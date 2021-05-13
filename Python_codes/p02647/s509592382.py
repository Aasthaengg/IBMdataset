n,k=map(int,input().split())
a=list(map(int,input().split()))
tu=0
td=0
if k>=40:
  a=[n]*n
else:
  for j in range(k):
    temp=[0]*n
    for i in range(n):
      td=max(i+1-a[i],1)
      temp[td-1]=temp[td-1]+1
      tu=min(i+1+a[i],n)
      if tu!=n:
        temp[tu]=temp[tu]-1
    a[0]=temp[0]
    for i in range(1,n):
      a[i]=a[i-1]+temp[i]
L=[str(t) for t in a]
L=" ".join(L)
print(L)