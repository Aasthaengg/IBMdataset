S = input()
# 'S': 晴 'R': 雨 #長さ3
count = 0
maximum = 0
for s in S:
  if s == 'R':
    count += 1
  else:
    count = 0
  maximum = max(maximum, count)
print(maximum)