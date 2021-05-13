import bisect

MOD=10**9+7
N=int(input())

clist=[]
for i in range(N):
  c=int(input())
  clist.append(c)  
#print(clist)

c2list=clist[:1]
for i in range(1,N):
  if clist[i]!=c2list[-1]:
    c2list.append(clist[i])
#print(c2list)
N2=len(c2list)

cdic={}
for i in range(N2):
  c=c2list[i]
  if not c in cdic:
    cdic[c]=[i]
  else:
    cdic[c].append(i)
#print(cdic)

dp=[1]+[0]*(N2-1)
for i in range(1,N2):
  c=c2list[i]
  dp[i]=dp[i-1]

  if len(cdic[c])>0:
    ind=bisect.bisect_left(cdic[c],i)
    if ind>0:
      dp[i]+=dp[cdic[c][ind-1]]
      #print(cdic[c],i,ind-1)
    
#print(dp)
print(dp[-1]%MOD)