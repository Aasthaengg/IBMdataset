n, *a = map(int, open(0).read().split())
a += 1,
m = 1000

def groupby():
  c, res = [], []
  for i in range(n + 1):
    if a[i-1] <= a[i]:
      pass
    else:
      res += [c[0], c[-1]],
      c = []
    c += a[i],
  return res

for i, j in groupby():
  m = m // i * j + m % i
print(m)