X,A,B=map(int,input().split())

if (A-B)>=0:
  print('delicious')
elif (A-B)<0 and (X-B+A)>=0:
  print('safe')
else:
  print('dangerous')