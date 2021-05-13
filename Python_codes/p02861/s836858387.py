import itertools
import math

def dist(x1, y1, x2, y2):
  return math.sqrt((x1-x2)**2 + (y1-y2)**2)

n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for p in itertools.permutations(xy):
  for i in range(n-1):
    ans += dist(*p[i], *p[i+1])

print(ans/math.factorial(n))