import sys
input = sys.stdin.buffer.readline
N = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
free = [0] * N
f = 0
if N == 1:
  if t[0] == a[0]:
    print(1)
  else:
    print(0)
  exit(0)
if max(a) != max(t):
  print(0)
  exit(0)
for i in range(1, N - 1):
  if t[i - 1] == t[i]:
    free[i] = t[i]
  if t[i - 1] != t[i]:
    if t[i] > a[i]:
      f = 1
      break
  if a[i] != a[i + 1]:
    if a[i] > t[i]:
      f = 1
      break
for i in range(N - 2, 0, -1):
  if a[i + 1] == a[i] and t[i - 1] == t[i]:
    free[i] = min(t[i], a[i])
  else:
    free[i] = 0
res = 1
if f:
  print(0)
  exit(0)
for i in range(N):
  res *= max(1, free[i])
  res %= mod
print(res)