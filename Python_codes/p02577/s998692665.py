num = list(input().split())

s = 0
for n in num:
  n = int(n)
  s += n

if s%9 == 0:
  print('Yes')
else:
  print('No')

