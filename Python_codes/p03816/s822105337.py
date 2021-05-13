def comp(n,s,a):
  cnt=1
  flag=s[0]
  for i in range(1,n):
    if flag==s[i]:cnt+=1
    else:
      flag=s[i]
      a+=[cnt]
      cnt=1
  a+=[cnt]
  return a
n=int(input())
a=sorted(list(map(int,input().split())))
b=comp(n,a,[])
l,r=0,len(b)-1
if l==r:b[0]=1
while l<r:
  while b[l]==1 and l<r:l+=1
  while b[r]==1 and l<r:r-=1
  if b[l]>1:
    b[l]-=1
    b[r]-=1
while b[l]>1:b[l]-=2
print(sum(b))