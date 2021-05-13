n = int(input())
s = [list(input()) for _ in range(2)]

mod = 10 ** 9 + 7
res = 1
flag = 0
skip = False
for i in range(n):
    if s[0][i] == s[1][i]:
        if flag == 0:
            res = res * 3 % mod
        elif flag == 1:
            res = res * 2 % mod
        
        flag = 1

    else:
        if skip:
            skip = False
            continue

        if flag == 0:
            res = res * 6 % mod
        elif flag == 1:
            res = res * 2 % mod
        else:
            res = res * 3 % mod
        
        flag = 2
        skip = True

print(res)