import sys
input=sys.stdin.readline
N,A,B=map(int,input().split())

hlist=[]
for i in range(N):
  hlist.append(int(input()))
mh=max(hlist)
#print(mh,hlist)

def isOK(m):
  if m==0:
    return False
  
  hlist2=list(hlist)
  for i in range(N):
    hlist2[i]-=m*B
  #print(m,hlist2)
  if max(hlist2)<=0:
    return True
  
  cnt=0
  for i in range(N):
    if hlist2[i]>0:
      cnt+=-(-hlist2[i]//(A-B))
  return cnt<=m

l,r=1,mh//B+1
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