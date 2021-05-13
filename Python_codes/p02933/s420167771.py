import sys
a = []
for l in sys.stdin:
    a.append(l)
a[0] = int(a[0])
if a[0] >= 3200:
  print(a[1])
else:
  print('red')