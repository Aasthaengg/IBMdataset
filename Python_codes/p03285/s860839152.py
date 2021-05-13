N = int(input())
flag = False
for a in range(25):
  for b in range(14):
    if 4*a+7*b==N:
      flag = True

if flag:
  print('Yes')
else:
  print('No')