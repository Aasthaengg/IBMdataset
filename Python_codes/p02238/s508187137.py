# coding: UTF-8
from collections import deque
n = int(input())
arrow = {}
visited = set()
d = {}
f = {}


for i in range(n):
  raw = list(map(int,input().split()))
  #print(raw)
  u = raw.pop(0)
  k = raw.pop(0)
  raw.sort()
  q = deque(raw)
  arrow[u] = q
  d[u] = -1
  f[u] = -1

def dfslocal(v,t,arrow,f,d):
  t += 1
  d[v] = t
  visited.add(v)
  #print("First visit to " + str(v) + " at " + str(t) + "!")
  while arrow[v]:
    k = arrow[v].popleft()
    if k not in visited:
      
      t = dfslocal(k,t,arrow,f,d)
  f[v] = t+1
  return t+1

def dfsglobal(arrow,f,d):
  t = 0
  for u in range(n):
    if u+1 not in visited:
      t = dfslocal(u+1,t,arrow,f,d)
  return t

t = dfsglobal(arrow,f,d)

for i in range(n):
  print(str(i+1) + " " + str(d[i+1]) + " " + str(f[i+1]))
