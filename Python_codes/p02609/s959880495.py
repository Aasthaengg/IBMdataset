n = int(input())
x = input()[::-1]

f = [0] * n
for i in range(1, n):
    p = bin(i).count("1")
    r = i % p
    f[i] = f[r] + 1

p = x.count("1")
p1, p2 = p + 1, p - 1

if p == 1:
    ii = x.index("1")
    x1 = pow(2, ii, p1)
    for i in range(n)[::-1]:
        if i == ii:
            print(0)
        else:
            r = (x1 + pow(2, i, p1)) % p1
            print(f[r] + 1)
    exit()

x1 = x2 = 0
for i in range(n):
    if x[i] == "1":
        x1 += pow(2, i, p1); x2 += pow(2, i, p2)
        x1 %= p1; x2 %= p2

for i in range(n)[::-1]:
    if x[i] == "0":
        r = (x1 + pow(2, i, p1)) % p1
    else:
        r = (x2 - pow(2, i, p2)) % p2
    print(f[r] + 1)
