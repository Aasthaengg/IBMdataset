n,m = tuple(map(int,input().split()))

p = [tuple(map(int,input().split())) for _ in [0]*m]

p = sorted(p)

ans = 0
area = (0,0)
for x,y in p:
  if area[0]<=x and x<area[1]:
    area = x,min(area[1],y)
  else:
    ans+=1
    area = x,y
print(ans)