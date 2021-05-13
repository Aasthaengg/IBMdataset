str = input()
s = str.count('R')

if s==0:
  print(0)
elif s == 1:
  print(1)
elif s == 2:
  if str == 'RRS' or str == 'SRR':
    print(2)
  else:
    print(1)
else:
  print(3)