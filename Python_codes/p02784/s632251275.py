h, n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
if h <= sum(a):
  print('Yes')
else:
  print('No')