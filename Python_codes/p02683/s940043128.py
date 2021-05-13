from itertools import combinations
import sys

n,m,x = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]

result = []
for i in range(1, n+1):
  cmb = [s for s in combinations(a, i)]
  for j in cmb:
    total = [0] * (m+1)
    for s in range(i):
      total = [x+y for (x,y) in zip(j[s], total)]
      result.append(total)
      
result.sort()
for k in result:
  price = k[0]
  del k[0]
  if min(k) >= x:
    print(price)
    sys.exit()

print('-1')