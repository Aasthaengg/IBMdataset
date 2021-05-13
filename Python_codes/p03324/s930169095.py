D,N=map(int,input().split())
i=0
c=0
while c<N:
  i+=1
  if (i*(100**D))%(100**(D+1))==0:
    continue
  c+=1
print(i*(100**D))  