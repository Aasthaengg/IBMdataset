import math
import sys
sys.setrecursionlimit(10**6)

n = int(input())
mincost = [None]*n

def cost(n,h):
  if (mincost[n-1] is not None):
    return mincost[n-1]
  elif (n == 1):
    mincost[n-1] = 0
  elif (n == 2):
    mincost[n-1] =  abs(h[1] - h[0])
  else:
    mincost[n-1] = min(cost(n-1,h) + abs(h[n-1]-h[n-2]), cost(n-2,h) + abs(h[n-1]-h[n-3]))
  return mincost[n-1]

h = [None]*n

h = list(map(int, input().split()))

print(cost(n,h))
