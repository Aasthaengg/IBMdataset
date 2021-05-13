import itertools

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

L = [i for i in range(N)]

sum = 0
LL = list(itertools.permutations(L))
for v in LL:
  x, y = xy[v[0]]
  for u in v[1:]:
    x2, y2 = xy[u]
    sum += ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5
    x, y = x2, y2
  
ave = sum / len(LL)
print(ave)