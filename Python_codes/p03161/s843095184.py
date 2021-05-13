import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k = map(int,readline().split())
h = list(map(int,readline().split()))

dp = [float('inf')]*n
dp[0] = 0

for i in range(1,n):
  for j in range(min(k,i)):
    dp[i] = min(dp[i], dp[i-1-j]+abs(h[i]-h[i-1-j]))

print(dp[n-1])