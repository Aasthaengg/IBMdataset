import sys

stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N = ri()
P = [ri() for _ in range(N)]

dp = [0] * (N+1)
for i in P:
    dp[i] = dp[i-1]+1

print(N-max(dp))
#40