import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N, M = IL()
abc = [IL() for _ in range(M)]

dp = [[MAX_INT]*N for _ in range(N)]
for a, b, c in abc:
  dp[a - 1][b - 1] = c
  dp[b - 1][a - 1] = c
for i in range(N):
  dp[i][i] = 0

for k in range(N):
  for i in range(N):
    for j in range(N):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
#print(dp)

used = [False]*M
cnt = 0
for edge in range(M):
  a, b, c = abc[edge]
  for i in range(N):
    for j in range(N):
      if dp[i][a - 1] + c + dp[b - 1][j] == dp[i][j]:
        used[edge] = True
        cnt += 1
        break
    else:
      continue
    break

#print(used)
print(M - cnt)