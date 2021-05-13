import sys

mod = 10**9 + 7
N = int(sys.stdin.readline())

stones = []
for _ in range(N):
    stones.append(int(sys.stdin.readline()))

left = {}
dp = [0 for _ in range(N+5)]
dp[0] = 1
for i in range(N):
    dp[i+1] = dp[i]
    # 同じ色が前回出現した位置
    c = stones[i]
    if c in left and 0 <= left[c] < i - 1:
        dp[i+1] += dp[left[c] + 1]
    
    dp[i+1] %= mod
    left[c] = i

print(dp[N])