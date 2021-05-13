a = list(map(int, input().split()))
a.sort()
if sum(a[:2]) == a[2]:
  print('Yes')
else:
  print('No')
