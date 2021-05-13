s = input()
t = input()
Y = True
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
  if s+i==t:
    print('Yes')
    Y = False
if Y:
  print('No')