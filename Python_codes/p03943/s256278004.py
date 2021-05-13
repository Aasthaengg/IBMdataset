candy = list(map(int, input().split()))

if candy.count(sum(candy)/2) == 1:
  print('Yes')
else:
  print('No')