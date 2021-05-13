input();a=list(map(int,input().split()))
for i,j in zip(a,sorted(a)):
  if abs(i-j)>1: print('No');break
else:
  print('Yes')