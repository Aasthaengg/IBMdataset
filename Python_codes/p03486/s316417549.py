a = input()
b = input()

A = sorted(a)
B = sorted(b)
B.reverse()

if(A < B):
  print('Yes')
else:
  print('No')