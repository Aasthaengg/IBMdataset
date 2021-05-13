n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a.reverse()

if x > sum(a):
  print(n - 1)
else:
  c = 0
  while x >= a[-1]:
    x -= a.pop()
    c += 1
    if c == n:
      break
  print(c)
