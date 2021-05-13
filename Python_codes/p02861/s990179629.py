import itertools
import math

n = int(input())
xy = [0]*n

for i in range(n):
  xy[i] = input().split()

t = []
  
for i in range(n):
  t.append(i)

t = list(itertools.permutations(t))
ans = 0

for i in range(len(t)):
  for j in range(n-1):
    tmp = t[i][j]
    tmp2 = t[i][j+1]
    ans += math.sqrt(((int(xy[tmp][0]) - int(xy[tmp2][0]))**2) + ((int(xy[tmp][1]) - int(xy[tmp2][1]))**2))
    
print(ans/len(t))