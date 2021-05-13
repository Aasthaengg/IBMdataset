from collections import deque
import sys, copy, itertools,heapq
input = sys.stdin.readline

n = int(input())
MAP = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
  MAP[i][i]=10**9


ans = 0
for i in range(n):
  for j in range(i+1,n):
    MAPP=[0]*n
    for k in range(n):
      MAPP[k]=MAP[i][k]+MAP[j][k]
    d = min(MAPP)
    if MAP[i][j] < d:
      ans += MAP[i][j]
    elif d < MAP[i][j]:
      print(-1)
      exit()
  
#print(MAP)
print(ans)