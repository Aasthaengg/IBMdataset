from collections import deque
import sys, copy, itertools,heapq
input = sys.stdin.readline

h,w = map(int,input().split())
TRANS = [list(map(int,input().split())) for i in range(10)]
A = [list(map(int,input().split())) for i in range(h)]

#print(TRANS)
#print(A)

#warshall_floyd  kijの順番に注意!!
for k in range(10):  #kは中継
  for i in range(10):  # iは始点
    for j in range(10):  #jは目的地
      if (TRANS[i][k] != float('inf')) and (TRANS[i][k] != float('inf')):
        TRANS[i][j] = min(TRANS[i][j],TRANS[i][k] + TRANS[k][j])
#print(TRANS)

ans = 0
for i in range(h):
  for j in range(w):
    a = A[i][j]
    if a==-1:
      continue
    else:
      ans += TRANS[a][1]

print(ans)