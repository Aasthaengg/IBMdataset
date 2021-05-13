a,b=map(int,input().split())
list=[4,6,9,11]
if a==2 or b==2:
  print('No')
elif a in list and b in list:
  print('Yes')
elif a not in list and b not in list:
  print('Yes')
else:
  print('No')
