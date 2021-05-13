a,b=map(int,input().split())
n=[a,b,a+b]
if len([i for i in n if i%3==0])>0:
  print('Possible')
else:
  print('Impossible')