n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = [0]+[float("inf")]*n
for i in range(n): dp[i+1] = min([float("inf")]+[dp[i+1-c_j] for c_j in c if c_j<=i+1])+1
print(dp[-1])
