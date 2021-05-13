from collections import Counter
n = int(input())
if n == 1:
  print(1)
else:
  XY = tuple(tuple(map(int, input().split())) for _ in range(n))
  L = []
  for i in range(n-1):
    for j in range(i+1, n):
      x1, y1 = XY[i]
      x2, y2 = XY[j]
      L.append((x1-x2, y1-y2))
      L.append((x2-x1, y2-y1))
  C = Counter(L)
  ans = n - C.most_common()[0][1]
  print(ans)