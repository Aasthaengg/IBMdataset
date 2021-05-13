a, b, c = map(int, input().split())
e = 0
for i in range(a):
  d = i + 1
  f = d
  L = []
  for j in range(len(str(d))):
    q, mod = divmod(f, 10)
    f = q
    L.append(mod)
  if b <= sum(L) and sum(L) <= c:
    e = e + d
print(e)