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
         
n, m = map(int, input().split())
es = []
for i in range(m):
  a, b, c = map(int, input().split())
  es.append([a-1, b-1, c*(-1)])
  
temp, d = find_negative_loop(0, n, m ,es)
if temp == d:
  print(d*(-1))
else:
  print('inf')