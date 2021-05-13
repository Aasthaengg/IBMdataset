N=int(input())
if N%2==0:
  print('{:.010f}'.format((N//2)/N))
else:
  print('{:.010f}'.format((N//2+1)/N))