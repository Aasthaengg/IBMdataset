import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

for x in range(1, 100):
  for y in range(1, 100):
    for z in range(1, 100):
      tmp = x*x + y*y + z*z + x*y + y*z + z*x
      if tmp <= n:
        dp[tmp] += 1

for i in range(1, n+1):
  print(dp[i])