import itertools
import math
 
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
 
avg = 0
permutations = list(itertools.permutations(range(N)))
for l in permutations:
  tmp = 0
  for i in range(len(l)-1):
    tmp += math.sqrt((xy[l[i+1]][0] - xy[l[i]][0])**2 + (xy[l[i+1]][1] - xy[l[i]][1])**2)
  avg += tmp

avg /= len(permutations)
print(avg)