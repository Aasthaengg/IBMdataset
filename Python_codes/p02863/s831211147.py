import sys
input = sys.stdin.readline
N, T = map(int, input().split())
t = [tuple(map(int, input().split())) for _ in range(N)]
t.sort()
dp = [0] * (T + 1)
for a, b in t:
  for i in range(T - 1, -1, -1):
    if i + a < T: dp[i + a] = max(dp[i + a], dp[i] + b)
    else: dp[-1] = max(dp[-1], dp[i] + b) 
print(max(dp))