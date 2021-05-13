s = input()
sum_ = 0
if s[0] == 'R':
  sum_ += 1
  if s[1] == 'R':
    sum_ += 1
    if s[2] == 'R':
      sum_ += 1
  else:
    sum_ = 1
else:
  if s[1] == 'R':
    sum_ += 1
    if s[2] == 'R':
      sum_ += 1
  else:
    if s[2] == 'R':
      sum_ = 1
print(sum_)