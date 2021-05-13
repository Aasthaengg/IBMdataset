n  = int(input())
a = list(map(int, input().split()))
total = sum(a)

def rain(i):
  rainfall = (total/2 - sum(a[:i-2:-2]) - sum(a[i+1::2])) * 2
  return int(rainfall)

i = 0
a.insert(0, a[n-1])
del a[n]
i += 1
r = []
r.append(rain(i))
a.append(a[0])
del a[0]

for i in range(1, n):
  rainfall = a[i-1] * 2 - r[i-1]
  r.append(rainfall)

for i in range(n):
  print(r[i])