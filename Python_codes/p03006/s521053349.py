import collections

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy.sort()

if N == 1:
  print(1)
  exit()

pq = []
for i in range(N):
  xi, yi = xy[i][0], xy[i][1]
  for j in range(i + 1, N):
    xj, yj = xy[j][0], xy[j][1]
    p, q = xj - xi, yj - yi
    pq.append((p, q))
#print(pq)

c = list(collections.Counter(pq).values())
c.sort()
print(N - c[-1])