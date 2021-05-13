mod=10**9+7
n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
edge1=[]
for i in range(n-1):
  edge1.append(arr1[i+1]-arr1[i])
edge2=[]
for i in range(m-1):
  edge2.append(arr2[i+1]-arr2[i])
c1=[0]*(m-1)
tmp=0
if (m-1)%2==0:
  for i in range((m-1)//2):
    tmp+=(m-1)-2*i
    c1[i]=tmp
    c1[-(i+1)]=tmp
else:
  for i in range((m-1)//2+1):
    tmp+=(m-1)-2*i
    if i==(m-1)//2:
      c1[i]=tmp
    else:
      c1[i]=tmp
      c1[-(i+1)]=tmp
area=0
if (m-1)%2==0:
  for i in range((m-1)//2):
    area+=edge2[i]*c1[i]
    area+=edge2[-(i+1)]*c1[i]
else:
  for i in range((m-1)//2+1):
    if i==(m-1)//2:
      area+=edge2[i]*c1[i]
    else:
      area+=edge2[i]*c1[i]
      area+=edge2[-(i+1)]*c1[i]
c2=[0]*(n-1)
tmp=0
if (n-1)%2==0:
  for i in range((n-1)//2):
    tmp+=(n-1)-2*i
    c2[i]=tmp
    c2[-(i+1)]=tmp
else:
  for i in range((n-1)//2+1):
    tmp+=(n-1)-2*i
    if i==(n-1)//2:
      c2[i]=tmp
    else:
      c2[i]=tmp
      c2[-(i+1)]=tmp
ans=0
if (n-1)%2==0:
  for i in range((n-1)//2):
    ans+=area*edge1[i]*c2[i]
    ans+=area*edge1[-(i+1)]*c2[i]
    ans%=mod
else:
  for i in range((n-1)//2+1):
    if i==(n-1)//2:
      ans+=area*edge1[i]*c2[i]
    else:
      ans+=area*edge1[i]*c2[i]
      ans+=area*edge1[-(i+1)]*c2[i]
print(ans%mod)