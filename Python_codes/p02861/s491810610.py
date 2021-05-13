import math
import itertools
n=int(input())
town=[]
for i in range(n):
  xy=list(map(int,input().split()))
  town.append(xy)
p=list(itertools.permutations(town,n))
d=0
for i in range(len(p)):
  for j in range(len(p[i])-1):
    d+=math.sqrt((p[i][j][0]-p[i][j+1][0])**2+(p[i][j][1]-p[i][j+1][1])**2)
print(d/len(p))