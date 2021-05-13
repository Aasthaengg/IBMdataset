import math

N,D = map(int,input().split())
XY = [tuple(map(int,input().split())) for _ in range(N)]

cnt = 0
for x, y in XY:
  if math.sqrt(x**2 + y**2) <= D:
    cnt += 1
    
print(cnt)