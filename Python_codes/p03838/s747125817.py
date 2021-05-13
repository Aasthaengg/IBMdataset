n,m = map(int, input().split())
diff = abs(abs(n) - abs(m))
res = diff

if abs(n) <= abs(m):
  if n < 0:
    res += 1
  if m < 0:
    res += 1
  print(res)

else:
  if n > 0:
    res += 1
  if m > 0:
    res += 1
  print(res)
