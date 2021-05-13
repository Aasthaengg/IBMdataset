h,w = map(int,input().split())
a = [[(i == "#")*1 for i in list(input())] for _ in range(h)]
dp = [[float("inf")]*w for _ in range(h)]
dp[0][0] = a[0][0]
def cnt(i0,j0,i1,j1):
  if a[i0][j0] == 0 and a[i1][j1] == 1:
    return 1
  return 0

for s in range(h+w):
  for i in range(s+1):
    j = s - i
    if i >= h or j >= w:
      continue
    if i < h-1:
      dp[i+1][j] = min(dp[i+1][j],dp[i][j]+cnt(i,j,i+1,j))
    if j < w-1:
      dp[i][j+1] = min(dp[i][j+1],dp[i][j]+cnt(i,j,i,j+1))
print(dp[-1][-1])