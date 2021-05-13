from itertools import combinations
n = int(input())
if n == 1:
  print(1)
  exit(0)
pos = []
for i in range(n):
  pos.append(tuple(map(int,input().split())))
ans = 1e100
def cost(p,q):
  ret = 0
  for i,j in pos:
    ret += 1 - ((i+p,j+q) in pos)
  return ret
for a,b in combinations(pos, 2):
  ans = min(ans, cost(a[0]-b[0],a[1]-b[1]))
print(ans)
