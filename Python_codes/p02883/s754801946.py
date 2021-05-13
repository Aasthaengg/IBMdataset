import sys
input = sys.stdin.readline
N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse = True)

def check(x):
  k = K
  for i in range(N):
    if a[i] * b[i] > x: k += (x - a[i] * b[i]) // b[i]
  return k >= 0

ok = 10 ** 12
ng = -1
while ok - ng > 1:
  m = (ok + ng) // 2
  if check(m): ok = m
  else: ng = m
print(ok)