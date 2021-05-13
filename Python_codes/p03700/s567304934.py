import sys
input = sys.stdin.readline
N, A, B = map(int, input().split())
h = [0] * N
for i in range(N): h[i] = int(input())
h.sort()

def check(x):
  t = [h[i] - x * B for i in range(N)]
  for i in range(N):
    if t[i] > 0:
      x -= -(-t[i] // (A - B))
      if x < 0: return False
  return x >= 0

ok = 10 ** 9
ng = 0
while ok - ng > 1:
  m = (ok + ng) // 2
  if check(m): ok = m
  else: ng = m
print(ok)