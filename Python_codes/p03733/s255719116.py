import sys
n, t, *lst = map(int, sys.stdin.read().split())
cur, res = 0, 0
for i in lst:
  if i <= cur + t:
    res += i - cur
  else:
    res += t
  cur = i
res += t
print(res)