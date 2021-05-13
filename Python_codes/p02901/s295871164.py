n,m = map(int, input().split())
a=[]
c=[]
for i in range(m):
    tmp,_=map(int, input().split())
    a.append(tmp)
    tmp=list(map(int, input().split()))
    bit = 0
    for b in tmp:
        bit+=(1<<(b-1))
    c.append(bit)

dp = [[10**9 for i in range(2**n)] for j in range(m+1)]
dp[0][0]=0

for i in range(m):
    cst = a[i]
    key=c[i]
    for s in range(2**n):
        dp[i+1][s] = min(dp[i+1][s], dp[i][s])
        dp[i+1][s|key] = min(dp[i+1][s|key], dp[i][s]+cst)

ans=dp[-1][-1]
if ans ==10**9:
    print(-1)
else:
    print(ans)