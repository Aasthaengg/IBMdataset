n=int(input())
x=input()
pc=[0]
m=2*10**5
for i in range(1,m+2):
  cnt=0
  j=i
  while i:
    cnt+=i%2
    i//=2
  pc+=[j%cnt]
f=[0]*(m+2)
for i in range(1,m+2):
  if pc[i]==0:f[i]=1
  else:f[i]=f[pc[i]]+1
cnt=x.count('1')
ix=int(x,2)
ixp=ix%(cnt+1)
ixm=ix%(cnt-1) if cnt-1 else 0
d=1<<(n-1)
for i in range(n):
  dp=pow(2,n-i-1,cnt+1)
  if cnt-1:dm=pow(2,n-i-1,cnt-1)
  if x[i]=='0':print(f[(ixp+dp)%(cnt+1)]+1)
  else:
    if cnt-1:print(f[(ixm-dm)%(cnt-1)]+1)
    else:print(0)