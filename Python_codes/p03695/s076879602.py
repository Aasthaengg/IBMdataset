n = int(input())
a = list(map(int, input().split()))

c = set()
k = 0
min_c = 1
max_c = 1
for i in range(n):
  if 1 <= a[i] <= 399:
    c.add(1)
  elif 400 <= a[i] <= 799:
    c.add(2)
  elif 800 <= a[i] <= 1199:
    c.add(3)
  elif 1200 <= a[i] <= 1599:
    c.add(4)
  elif 1600 <= a[i] <= 1999:
    c.add(5)
  elif 2000 <= a[i] <= 2399:
    c.add(6)
  elif 2400 <= a[i] <= 2799:
    c.add(7)
  elif 2800 <= a[i] <= 3199:
    c.add(8)
  elif a[i] >= 3200:
    k += 1

if k != n:
  min_c = len(list(c))
  max_c = len(list(c)) + k
else:
  min_c = 1
  max_c = n
print(min_c, max_c)