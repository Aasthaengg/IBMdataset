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

cldic={}
dp=[0]*(N2-1)+[1]
for i in range(N2):
  c=c2list[i]
  dp[i]=dp[i-1]
  if c in cldic:
    dp[i]+=dp[cldic[c]]      
  cldic[c]=i
    
#print(dp)
print(dp[-1]%MOD)