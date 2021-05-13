N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]

ans = 0

for i in range(N-1):
  x1,y1 = xy[i]
  for j in range(i+1,N):
    x2,y2 = xy[j]
    p = x2-x1
    q = y2-y1
    cost = 0
    for x,y in xy:
      if [x-p,y-q] in xy:
        cost += 1
    ans = max(ans,cost)
    
print(N-ans)