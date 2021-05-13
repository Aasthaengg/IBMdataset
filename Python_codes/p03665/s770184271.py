n, p = map(int, input().split())
a = list(map(int, input().split()))

m = len([x for x in a if x & 1])

if m == 0:
  if p == 0:
    ans = 2 ** n
  else:
    ans = 0
else:
  ans = 2 ** (n - 1)

print(ans)