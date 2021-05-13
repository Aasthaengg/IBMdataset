n,k=map(int, input().split())
a=list(map(int, input().split()))
alist=[]
cnt=0
i=1
blist=[0]*(n+1)
while blist[a[i-1]]==0:
  i=a[i-1]
  alist.append(i)
  blist[i]=1
  cnt+=1
loop1=alist.index(a[i-1])
if k<loop1+1:
  print(alist[k-1])
else:
  print(alist[((k-loop1-1)%(cnt-loop1))+loop1])