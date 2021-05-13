a,b=map(int, input().split())
c=int(str(a)+str(b))
counter=0
for i in range(c):
  if i*i==c:
    counter=1
if counter==0:
  print('No')
else:
  print('Yes')