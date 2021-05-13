import sys
from collections import deque
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N,T = IL()
ab = [IL() for i in range(N)]
ab.sort()

ans = 0
dp = [[0]*T for i in range(N+1)]
for i in range(1,N+1):
  a,b = ab[i-1]
  for j in range(T):
    if 0 <= j-a < T:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-a] + b)
    else:
      dp[i][j] = dp[i-1][j]
  else:
    ans = max(ans, dp[i-1][-1] + b)
print(ans)