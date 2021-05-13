n,*a=map(int,open(0).read().split())
a=[i%4 for i in a]
if a.count(2)>0:
  print('Yes' if a.count(0)>=a.count(1)+a.count(3) else 'No')
else:
  print('Yes' if 1+a.count(0)>=a.count(1)+a.count(3) else 'No')