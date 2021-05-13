N, K = map(int, raw_input().split())
A = map(int, raw_input().split())
dp = [False]
for i in range(1, K+1):
    dp.append(not all(dp[i-x] for x in A if i >= x))
print "First" if dp[K] else "Second"