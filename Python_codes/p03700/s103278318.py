import sys
input = sys.stdin.readline
N, A, B = map(int, input().split())
h = []
for _ in range(N):
  h.append(int(input()))
h.sort()
def explosive(x):
  c = 0
  for i in range(N):
    if h[i] > x * B:
      c += -(-(h[i] - x * B) // (A - B))
  if c <= x: return True
  else: return False
ng = 0
ok = 10 ** 9
m = 0
while ok - ng > 1:
  m = (ng + ok) // 2
  #print(m, explosive(m))
  if explosive(m):
    ok = m
  else:
    ng = m
print(ok)