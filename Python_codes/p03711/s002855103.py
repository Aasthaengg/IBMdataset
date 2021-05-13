import sys
x,y=map(int, input().split())
if x==2 or y==2:
  print('No')
  sys.exit()

a=[4,6,9,11]
if (x in a) and (y in a):
  print('Yes')
elif (x not in a) and (y not in a):
  print('Yes')
else:
  print('No')
