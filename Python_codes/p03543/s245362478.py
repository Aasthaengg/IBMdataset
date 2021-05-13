s=input()
a=[i for i in s]
if len(set(a[:3]))==1 or len(set(a[1:]))==1:
  print('Yes')
else:
  print('No')