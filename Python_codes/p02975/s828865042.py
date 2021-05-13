import collections
n=int(input())
a=list(map(int,input().split()))
b=0
for i in a:
  b^=i
c=collections.Counter(a)
if len(c)>3:
  print('No')
elif len(c)==1:
  if a[0]==0:
    print('Yes')
  else:
    print('No')
elif b==0:
  print('Yes')
else:
  print('No')