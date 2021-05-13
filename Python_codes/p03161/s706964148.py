N,K = [int(c) for c in input().split()]
h = [int(c) for c in input().split()]

dp=[0]*N
for i in range(1,N):
    dp[i] = min([dp[j] + abs(h[i]-h[j]) for j in range(max(0,i-K),i) ])
print(dp[-1])

