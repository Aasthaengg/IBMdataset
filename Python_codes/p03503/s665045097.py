n=int(input())
f = [tuple(map(int, input().split( ))) for _ in range(n)]
p = [tuple(map(int, input().split( ))) for _ in range(n)]

bit = 1<<10
ans = -10**10
for i in range(1,bit):
    tmp = 0
    for j in range(n):
        cj = 0
        for k in range(10):
            cj+= f[j][k] & (i>>k)
        tmp += p[j][cj]
    ans = max(ans,tmp)
print(ans)