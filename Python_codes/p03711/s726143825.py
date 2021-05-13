x,y=map(int,input().split())

a=[1,3,5,7,8,10,12]
b=[4,6,9,11]
c=[2]

for i in a:
  if x==i:
    x='a'
  if y==i:
    y='a'

for i in b:
  if x==i:
    x='b'
  if y==i:
    y='b'

for i in c:
  if x==i:
    x='c'
  if y==i:
    y='c'

if x==y:
  print('Yes')
else:
  print('No')
