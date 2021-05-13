n = int(input())
l = sorted([int(x) for x in input().split()], reverse=True)

if l[0] < sum(l[1:]):
  print('Yes')
else:
  print('No')