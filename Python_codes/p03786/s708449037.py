n, *A = map(int, open(0).read().split())
A.sort()
s = 0
for a in A:
  if 2*s < a:
    c = 1
  else:
    c += 1
  s += a
print(c)