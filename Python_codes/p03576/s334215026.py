import sys
import itertools

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
XY = [lr() for _ in range(N)]
XY.sort()
answer = float('inf')
# 端の4点、まずはx軸の2点を選ぶ
for left,right in itertools.combinations(range(N),2):
  xleft = XY[left][0]
  xright = XY[right][0]
  pts = sorted(XY[left:right+1], key = lambda xy: xy[1])
  if len(pts) < K:
    continue
  for D in range(len(pts) - K + 1):
    y_max = pts[D+K-1][1]
    y_min = pts[D][1]
    area = (y_max - y_min) * (xright - xleft)
    if area < answer:
      answer = area
    
print(answer)
