*a, = map(int, open(0).read().split())
c = 0
for i, j in enumerate(a):
  c += (a[j:j+1] == [i])*(i > 0)
print(c // 2)