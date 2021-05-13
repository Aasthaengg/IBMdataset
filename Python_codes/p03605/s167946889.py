N=int(input())

N1=N//10
N0=N%10

if N1==9 or N0==9:
  print('Yes')
else:
  print('No')