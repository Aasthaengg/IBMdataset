n = int(input())
f = [list(map(int,input().split())) for i in range(n)]
p = [list(map(int,input().split())) for i in range(n)]
ans = -10**10
for i in range(1,2**10):
    a = 0
    for j in range(n):
        a += p[j][sum(i>>k&1 and f[j][k] for k in range(10))]
    ans = max(ans,a)
print(ans)
