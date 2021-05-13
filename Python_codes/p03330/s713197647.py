from itertools import permutations as per
n,c = map(int,input().split())
d = [tuple(map(int,input().split())) for i in range(c)]
g = [[0]*c,[0]*c,[0]*c]
for i in range(1,n+1):
  ci = tuple(map(int,input().split()))
  for j in range(1,n+1):
    g[(i+j)%3][int(ci[j-1])-1] += 1
m = 10 ** 10
for i in per(range(c),3):
  e = 0
  for j in range(3):
    for o in range(c):
      e += g[j][o]*d[o][i[j]-1]
  m = min(m,e)
print(m)