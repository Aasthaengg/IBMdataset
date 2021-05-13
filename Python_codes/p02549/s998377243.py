n, k = map(int, input().split())
dp=[0]*(n+1)
dp[1] = 1

rui=[0]*(n+1)
rui[1] = 1
p = 998244353
lr=[]
for i in range(k):
    lr.append(list(map(int, input().split())))

for i in range(2,n+1):
    for l, r in lr:
        dp[i] += rui[max(i-l, 0)] - rui[max(i-r-1, 0)]
        dp[i] %= p
    rui[i] = rui[i-1] + dp[i]
    rui[i] %= p
print(dp[n])
