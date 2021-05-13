N, K = map(int, input().split())
a = list(map(int, input().split()))

dp = [-1] * (K+1)
ans = int(0)

for i in a:
    dp[i] = int(1)
#print(dp)
for i in range(K+1):
    v = int(-1)
    for j in a:
        if i>j and dp[i-j]==-1:
            v = int(1)
    if dp[i]==-1:
        dp[i] = v

if dp[K]==1:
    ans = "First"
else:
    ans = "Second"

print(ans)