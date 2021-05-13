n = int(input())
a = [[0]+list(map(int,input().split())) for _ in range(2)]
for i in range(n):
    a[0][i+1] += a[0][i]
for i in range(n,0,-1):
    a[1][i-1] += a[1][i]
ans = 0
for i in range(1,n+1):
    ans = max(ans, a[0][i]+a[1][i])
print(ans)