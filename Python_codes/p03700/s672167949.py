import sys
input=sys.stdin.readline
N,A,B=map(int,input().split())

hlist=[]
mh=0
for i in range(N):
  h=int(input())
  hlist.append(h)
  mh=max(mh,h)
#print(mh,hlist)

res_dic={0:False}
def isOK(m):
  if m in res_dic:
    return res_dic[m]
  
  h2list=[]
  mh2=-float("inf")
  for i in range(N):
    h2=hlist[i]-m*B
    h2list.append(h2)
    mh2=max(h2,mh2)
  if mh2<=0:
    res_dic[m]=True
    return res_dic[m]
  
  cnt=0
  for i in range(N):
    if h2list[i]>0:
      cnt+=-(-h2list[i]//(A-B))
      
  res_dic[m]=(cnt<=m)
  return res_dic[m]

l,r=1,-(-mh//B)
while l<=r:
  mid=(l+r)//2
  #print(l,mid,r)
  if not isOK(mid-1) and isOK(mid):
    print(mid)
    break
  elif isOK(mid-1):
    r=mid-1
  else:
    l=mid+1