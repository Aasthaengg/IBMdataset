a,b,c,d=map(int,input().split())
if a+b==c+d:
  print('Balanced')
else:
  print('RLiegfhtt'[a+b>c+d::2])