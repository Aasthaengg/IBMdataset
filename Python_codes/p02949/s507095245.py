import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find_negative_loop(s,n,w,es):
  # s: start
  # n: number of nodes
  # w: number of edges
  # es[i]: from, to, cost
  
  # d: shortest dist of s -> i
  inf = float('inf')
  d = [inf for _ in range(n)]
  d[s] = 0
  for i in range(2*n):
    for j in range(w):
      p, q, r = es[j]
      if d[p] != inf and (d[q] > d[p] + r):
        d[q] = d[p] + r
        if i >= n:
          d[q] = (-1)*inf
    if i == n-1:
      temp = d[-1]
  return temp, d[-1]
         

n, w, p = map(int, input().split())
es = []
for i in range(w):
  x, y, z = map(int, input().split())
  es.append([x-1, y-1, (z-p)*(-1)])
  
temp, d = find_negative_loop(0, n, w ,es)
if temp == d:
  print(min(0, d)*(-1))
else:
  print('-1')