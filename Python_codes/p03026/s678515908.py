#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
G = [[] for i in range(n)]
for i in range(n-1):
  a,b = map(int,input().split())
  a-=1;b-=1
  G[a].append(b)
  G[b].append(a)
C = list(map(int,input().split()))
C.sort(reverse = True)
ans = [0]*n
ans[0] = C[0]
que = collections.deque([0])
i = 1
M = 0
while que:
  node = que.popleft()
  for vi in G[node]:
    if ans[vi] == 0:
      ans[vi] = C[i]
      i += 1
      que.append(vi)
      M += min(ans[vi],ans[node])
print(M)
print(*ans)