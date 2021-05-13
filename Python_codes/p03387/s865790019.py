a = list(map(int, input().split()))
a.sort()
d = a[2] * 2 - a[0] - a[1]
if d % 2 == 1:
  d += 4
print(d//2)