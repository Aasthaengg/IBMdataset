from itertools import permutations
from math import sqrt

n = int(input())
position = [tuple(map(int,input().split())) for _ in range(n)]

def dist_calc(i,j):
  return sqrt(pow(position[i][0]-position[j][0],2)
              +pow(position[i][1]-position[j][1],2))

ans = 0
mean = 0
for tmp in permutations(range(n)):
  for j in range(n-1):
    ans += dist_calc(tmp[j],tmp[j+1])
  mean += 1
print(ans/mean) 