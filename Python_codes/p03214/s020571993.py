n, *a = map(int, open(0).read().split())
s = sum(a)
m = float("inf")
for i, j in enumerate(a):
  t = abs(s - n*j)
  if t < m:
    m = t
    k = i
print(k)