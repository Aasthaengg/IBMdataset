n,m = map(int,input().split())
down,up = 0,10**5
for _ in range(m):
  l,r = map(int,input().split())
  down = max(l,down)
  up = min(r,up)
print(max(up-down+1,0))