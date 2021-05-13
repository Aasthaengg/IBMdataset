N=int(input())
A=int(input())
b=N//500
c=N-500*b
if c<=A:
  print('Yes')
else:
  print('No')