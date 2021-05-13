a = list(map(int,open(0).read().split()))
i = 100
c = 0
while i < a[0]:
  i +=  i//100
  c += 1
print(c)