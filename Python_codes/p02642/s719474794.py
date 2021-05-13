import sys

n = int(input())

A = list(map(int, input().split()))

m = max(A)

C = [0] * (10**6 + 1)

dp = [True] * m

for a in A:
  if C[a] > 0:
    C[a] += 1
    continue
  C[a] += 1
  i = 2
  while a * i <= m:
    dp[a*i - 1] = False
    i += 1
    
ans = 0

for a in A:
  if C[a] < 2 and dp[a - 1] == True:
    ans += 1

print(ans)