n,a,b = map(int,input().split())     

t = list(map(int,input().split()))

t.sort()

dp=[0]*n

for i in range(1,n):
    dp[i] += dp[i-1]+min((t[i]-t[i-1])*a,b)
print(dp[-1])