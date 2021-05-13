x,y=map(int,input().split())
s0=1<<(x-1)|1<<(y-1)
s1=sum(list(map(lambda x:1<<(x-1),[1,3,5,7,8,10,12])))&s0
s2=sum(list(map(lambda x:1<<(x-1),[4,6,9,11])))&s0
s3=sum(list(map(lambda x:1<<(x-1),[2])))&s0

if s1==s0 or s2==s0 or s3==s0:
  print('Yes')
else:
  print('No')
