from itertools import product
n,c = map(int,input().split())
cost = [list(map(int,input().split())) for i in range(c)]
grid = [list(map(int,input().split())) for i in range(n)]
sum0 = []
sum1 = []
sum2 = []
for color in range(c):
  s0,s1,s2 = 0,0,0
  for i in range(n):
    for j in range(n):
      x = grid[i][j]-1
      if (i+j)%3 == 0:
        s0 += cost[x][color]
      elif (i+j)%3 == 1:
        s1 += cost[x][color]
      else:
        s2 += cost[x][color]
  sum0.append((s0,color))
  sum1.append((s1,color))
  sum2.append((s2,color))
ans = 10**18
for a,b,c in product(sum0,sum1,sum2):
  if a[1] != b[1] and b[1] != c[1] and c[1] != a[1]:
    ans = min(ans,a[0]+b[0]+c[0])
print(ans)