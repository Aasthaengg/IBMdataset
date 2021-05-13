import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mod = 10 ** 9 + 7
t = [10 ** 10 for _ in range(N)]
t[0] = a[0]
t[-1] = b[-1]
s = set()
s.add(0)
s.add(N - 1)
if a[0] > b[0] or (a[-1] < b[-1]):
  print(0)
  exit(0)
if a[-1] != b[0]:
  print(0)
  exit(0)
for i in range(N - 1):
  if a[i + 1] > a[i]:
    if t[i + 1] > 0 and (t[i + 1] in range(a[i + 1])):
      print(0)
      exit(0)
    s.add(i + 1)
    t[i + 1] = a[i + 1]
  else: t[i + 1] = min(t[i + 1], t[i])
#print(t)
for i in range(N - 1, 0, -1):
  if b[i - 1] > b[i]:
    if t[i - 1] > 0 and (t[i - 1] in range(b[i - 1])):
      print(0)
      exit(0)
    s.add(i - 1)
    t[i - 1] = b[i - 1]
  else: t[i - 1] = min(t[i - 1], t[i])
#print(t)
res = 1
for i in range(N):
  if i in s: continue
  res *= t[i]
  res %= mod
print(res)