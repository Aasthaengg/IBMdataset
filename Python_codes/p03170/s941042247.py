import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, k = map(int, input().split())
A = list(map(int, input().split()))
dp = [-1]*(k+1)
def dfs(k):
  if dp[k] != -1:
    return dp[k]
  for a in A:
    if k-a >= 0 and dfs(k-a) == 0:
      dp[k] = 1
      return 1
  dp[k] = 0
  return 0
result = dfs(k)
if result:
  print("First")
else:
  print("Second")