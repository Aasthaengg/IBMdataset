N,*L = map(int, open(0).read().split())
if all(c%2==0 for c in L):
  print('second')
else:
  print('first')