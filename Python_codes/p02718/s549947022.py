N, M = list(map(int,input('').split(' ')))
A = sorted(list(map(int,input('').split(' '))), reverse=True)
pts = sum(A)
if A[M-1]>=(pts/(4*M)):
  print('Yes')
else:
  print('No')