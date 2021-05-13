lst = list(map(int, input().split()))
total = 0
for i in lst:
  total += i
if total>= 22:
  print('bust')
else:
  print('win')