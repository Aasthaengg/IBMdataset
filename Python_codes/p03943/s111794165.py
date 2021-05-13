a,b,c=map(int,input().split())
x=[a,b,c]
y=sorted(x)
if (y[0]+y[1])==y[2]:
  print('Yes')
else:
  print('No')