import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

def check(x):
  c = 0
  for y in a:
    ok = N
    ng = -1
    while ok - ng > 1:
      m = (ok + ng) // 2
      if a[m] + y >= x: ok = m
      else: ng = m
    c += N - ok
  return c >= M

ok = 0
ng = 10 ** 6
while ng - ok > 1:
  m = (ok + ng) // 2
  if check(m): ok = m
  else: ng = m

l = ok + 1
cs = [0] * (N + 1)
for i in range(N): cs[i + 1] = cs[i] + a[i]

res = 0
c = 0
for x in a:
  ok = N
  ng = -1
  while ok - ng > 1:
    m = (ok + ng) // 2
    if a[m] + x >= l: ok = m
    else: ng = m
  c += N - ok
  res += cs[-1] - cs[ok] + x * (N - ok)

print(res + (l - 1) * (M - c))