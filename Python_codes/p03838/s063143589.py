x,y = map(int,input().split())
ans = 10**18
dx = [1,1,-1,-1]
dy = [1,-1,1,-1]

for i in range(4):
  tx = x * dx[i]
  ty = y * dy[i]
  if tx <= ty:
    ans = min(ans,ty-tx + (2-dx[i]-dy[i])//2)
print(ans)