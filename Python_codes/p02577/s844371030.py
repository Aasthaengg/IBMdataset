input_ = input()
sum_ = 0
for i in input_:
  sum_ += int(i)
if sum_ % 9 == 0:
  print('Yes')
else:
  print('No')