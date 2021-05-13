import sys

H, N = map(int, input().split())
ABs = [(0,0)]

for _ in range(N):
  a,b = map(int, input().split())
  ABs.append((a,b))
  
memo = [[sys.maxsize]*(H+1) for _ in range(N+1)]
memo[0][H] = 0

for i in range(1,N+1):
  for j in range(H,0,-1):
    if j + ABs[i][0] <= H:
      memo[i][j] = min(memo[i-1][j], memo[i][j+ ABs[i][0]] + ABs[i][1])
    else:
      memo[i][j] = min(memo[i][j], memo[i-1][j])
    if j - ABs[i][0] <= 0:
      memo[i][0] = min(memo[i-1][0], memo[i][0], memo[i][j]+ABs[i][1])
      
print(memo[N][0])