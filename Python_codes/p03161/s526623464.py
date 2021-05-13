from math import inf

n,k=map(int,input().split())
h=list(map(int,input().split()))
cost=[0]*n
cost[-2]=abs(h[-1]-h[-2])
for i in range(n-3,-1,-1):
  mini=inf
  for j in range(1,k+1):
    
    if i+j<n:
      #print(i,i+j,abs(h[i]-h[i+j])+cost[i+j])
      mini=min(abs(h[i]-h[i+j])+cost[i+j],mini)
  cost[i]=mini
print(cost[0])