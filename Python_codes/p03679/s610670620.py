x,a,b=map(int,input().split())
if b in range(a+1):
  print('delicious')
elif b in range(a,x+a+1):
  print('safe')
elif b>a+x:
  print('dangerous')