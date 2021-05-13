from collections import defaultdict
N = int(input())
d = defaultdict(int)
XY = sorted([list(map(int,input().split())) for _ in range(N)])
for i in range(N):
  for j in range(i):
    d[(XY[i][0] - XY[j][0], XY[i][1] - XY[j][1])] += 1
print(N - max(d.values(), default=0))