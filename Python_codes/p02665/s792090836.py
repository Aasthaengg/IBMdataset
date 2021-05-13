n=int(input())
a=list(map(int,input().split()))
if n==0 and a[0]!=1:
  print(-1)
  exit()
b=[a[0]==0]
for i in a[1:]:
  b+=[2*b[-1]-i]
  if b[-1]<0:
    print(-1)
    exit()
b.pop()
ans=root=a[-1]
a=a[::-1]
b=b[::-1]
for i,j in zip(a[1:],b):
  root=min(root,j)+i
  ans+=root
print(ans)