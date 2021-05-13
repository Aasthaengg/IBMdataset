import sys
readline = sys.stdin.readline

W,H,N = map(int,readline().split())
minX = 0
minY = 0
maxX = W
maxY = H

for i in range(N):
  x,y,a = map(int,readline().split())
  if a == 1:
    minX = max(minX,x)
  elif a == 2:
    maxX = min(maxX,x)
  elif a == 3:
    minY = max(minY,y)
  elif a == 4:
    maxY = min(maxY,y)

print(max(0,maxX - minX) * max(0,maxY - minY))