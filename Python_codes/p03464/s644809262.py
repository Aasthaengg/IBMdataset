k=int(input())
a=list(map(int,input().split()))
a.reverse()
d=[2,2]
f=True
for i in a:
  d[0]=((d[0]-1)//i+1)*i
  d[1]=d[1]//i*i+i-1
  if d[0]>d[1]:
    f=False
if f:
  print(d[0],d[1])
else:
  print(-1)