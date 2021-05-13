#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
G = [[] for i in range(n)]
F = [-1]*n
AB = []
for i in range(n-1):
  a,b = map(int,input().split())
  a-=1;b-=1
  G[a].append(b)
  G[b].append(a)
  AB.append((a,b))
C = sorted(map(int,input().split()),reverse = True)
for i in range(n):
  G[i].sort(key = lambda x:len(G[x]))
m = max(range(n),key = lambda x: len(G[x]))
count = 1
que = collections.deque()
que.append(m)
F[m] = C[0]
while que:
  node = que.popleft()
  for vi in G[node]:
    if F[vi] != -1: continue
    F[vi] = C[count]
    count += 1
    que.append(vi)

for a,b in AB:
  ans += min(F[a],F[b])
print(ans)
print(*F)
# print(C)

