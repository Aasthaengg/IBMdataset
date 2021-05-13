x,a,b=map(int,input().split())
if x+a<b:
  print('dangerous')
elif a+x>=b and a<b:
  print('safe')
else:
  print('delicious')