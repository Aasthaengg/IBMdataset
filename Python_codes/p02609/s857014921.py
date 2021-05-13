n = int(input())
x_bin = input()
x = int(x_bin, 2)

pc = x_bin.count('1')
pc_p = pc + 1
pc_m = pc - 1

if pc == 1:
    for i, v in enumerate(x_bin):
        if v == '1':
            print(0)
        else:
            if i != n-1:
                if x_bin[-1] == '0':
                    print(1)
                else:
                    print(2)
            else:
                print(2)
    exit()

p = {0: 1}
m = {0: 1}
for i in range(1, n):
    p[i] = p[i-1]*2 % pc_p
    m[i] = m[i-1]*2 % pc_m

rest = {0: 0}
for i in range(1, pc + 1):
    rest[i] = rest[i % bin(i).count('1')] + 1

x_p = x % pc_p
x_m = x % pc_m

for i in range(n, 0, -1):
    if x_bin[n-i] == '1':
        a = (x_m - m[i-1]) % pc_m
        print(rest[a] + 1)
    else:
        a = (x_p + p[i-1]) % pc_p
        print(rest[a] + 1)
