X,Y=map(str,input().split())
a=['A','B','C','D','E','F']
b=['10','11','12','13','14','15']

for i in range(6):
  if X==a[i]:
    X=b[i]
  if Y==a[i]:
    Y=b[i]
    
if X<Y:
  print('<')
elif X==Y:
  print('=')
else:
  print('>')