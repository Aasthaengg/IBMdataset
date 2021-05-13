N=int(input())
pn=list(map(int,input().split()))
check=[0]*N
for i in range(0,N):
  if pn[i]!=(i+1):
    check[i]=1 #ok
i=0
count=0
while i<N-1:
  if check[i]==0:#if ng
    pn[i],pn[i+1]=pn[i+1],pn[i]
    count+=1
    check[i],check[i+1]=1,1
  i+=1
  pass
if check[i]==0:count+=1
print(count)

