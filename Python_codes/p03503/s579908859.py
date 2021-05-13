n = int(input())
f = [list(map(int,input().split())) for i in range(n)]
p = [list(map(int,input().split())) for i in range(n)]

s = [list(map(int,bin(x)[2:].zfill(10))) for x in range(1,2**10)]
c = 0
ans = 0
max = -1000000000
for k in range(2**10-1):
    for i in range(n):
        for j in range(10):
            c += f[i][j]*s[k][j]
        ans += p[i][c]
        c=0
    if ans > max:
        max = ans
    ans = 0
print(max)
