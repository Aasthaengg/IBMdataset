n=int(input())
a=list(map(int,input().split()))
b=[a[0]]
f=-1
for i in a:
  if b[-1]<i:
    if f==1:b[-1]=i
    else:
      b.append(i)
      f=1
  if b[-1]>i:
    if f==-1:b[-1]=i
    else:
      b.append(i)
      f=-1
if f==-1:del b[-1]
if len(b)==0:exit(print(1000))
ans=1000
for i in range(0,len(b),2):
  bb=ans//b[i]
  ans-=bb*b[i]
  ans+=bb*b[i+1]
print(ans)
