D,G=map(int,input().split())
p=[]
c=[]
for i in range(D):
  p1,c1=map(int,input().split())
  p.append(p1)
  c.append(c1)
ans=sum(p)
for i in range(2**D):
  num=0
  point=0
  flag=[0]*D
  for j in range(D):
    if(i>>j&1):
      num+=p[j]
      flag[j]=1
      point+=(j+1)*100*p[j]+c[j]
  if(point<G):
    sitt=flag[::-1]
    loc=D-1-sitt.index(0)
    k=0
    while(point<G):
      num+=1
      k+=1
      point+=(loc+1)*100
    if(k<p[loc]):
      ans=min(ans,num)
  else:
    ans=min(ans,num)
  #print(loc)
print(ans)