n=int(input())
x=list(map(int,input().split()))
a=[]
for i in x:
  if i%2==1:
      a+=[i]
if len(a)%2==1:
  print('NO')
else:
  print('YES')