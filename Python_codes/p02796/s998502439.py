import bisect
N=int(input())

rllist=[]
for _ in range(N):
  X,L=map(int,input().split())
  rllist.append((X+L,X-L))
rllist.sort()
#print(rllist)

dp=[0]*N
for i in range(N):
  r,l=rllist[i]
  
  pos=bisect.bisect(rllist,(l,float("inf")))
  #print(i,pos)
  dp[i]=max(dp[i-1],dp[pos-1]+1)
  
#print(dp)
print(dp[-1])