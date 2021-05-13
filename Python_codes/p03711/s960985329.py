x,y=map(int,input().split())

a=[1,3,5,7,8,10,12]
b=[4,6,9,11]
c=[2]

x_group=''
y_group=''

for i in range(len(a)):
  if x==a[i]:
    x_group='a'
  if y==a[i]:
    y_group='a'
    
for i in range(len(b)):
  if x==b[i]:
    x_group='b'
  if y==b[i]:
    y_group='b'

for i in range(len(c)):
  if x==c[i]:
    x_group='c'
  if y==c[i]:
    y_group='c'
    
if x_group==y_group:
  print('Yes')
else:
  print('No')