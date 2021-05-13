import sys
import numpy as numpy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

N,M = map(int,input().split())
XY = [[] for i in range(N + 1)]

path = [-1] * (N + 1)

for i in range(M):
  x,y = map(int,input().split())
  XY[x - 1].append(y - 1)

  
def recur(n):
  if path[n] != -1:
    return path[n]
  
  elif XY[n] == []:
    path[n] = 0
    return path[n]
        
  else:
    ret = 0
    for chi in XY[n]:
      ret = max(ret,recur(chi) + 1)
    
    path[n] = ret
    return path[n]
    
for i in range(N):
  recur(i)

print(max(path))