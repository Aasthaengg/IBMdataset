x,a,b = map(int,input().split())
aa = abs(x-a)
bb = abs(x-b)
if aa<bb:
  print('A')
else:
  print('B')