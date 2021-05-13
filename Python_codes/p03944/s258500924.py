W,H,N = map(int,input().split())
XYA = [list(map(int,input().split())) for _ in range(N)]

E = [0,W,0,H]

for x,y,a in XYA:
  a -= 1
  XY = [x,y]
  if a % 2 == 0:
    E[a] = max(E[a],XY[a//2])
  else:
    E[a] = min(E[a],XY[a//2])

ans = 0
if E[0] < E[1] and E[2] < E[3]:
  ans = (E[1] - E[0]) * (E[3] - E[2])
  
print(ans)


