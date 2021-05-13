n,m = map(int,input().split())
p = []
for k in range(m):  
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    key = 0
    for i in c:
        key += 2**(i-1)
    p.append([a,key])
inf = 10**9
dp = []
for u in range(m+1):
    dp.append([inf for i in range(2**n)])
dp[0][0] = 0
for i in range(m):
    for k in range(2**n):
        dp[i+1][k] = dp[i][k]
    for k in range(2**n):
        dp[i+1][k|p[i][1]] = min(dp[i][k|p[i][1]],dp[i][k]+p[i][0],dp[i+1][k|p[i][1]])
if dp[-1][-1] == inf:
    print(-1)
else:
    print(dp[-1][-1])