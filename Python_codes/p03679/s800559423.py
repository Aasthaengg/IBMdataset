x,a,b=map(int,input().split())
if b-a<=x and b-a>0:
  print('safe')
elif b-a<=x:
  print('delicious')
else:
  print('dangerous')