input();a=list(map(int,input().split()));b=sorted(a)
for i,j in zip(a,b):
  if abs(i-j)>1: print('No');break
else:
  print('Yes')