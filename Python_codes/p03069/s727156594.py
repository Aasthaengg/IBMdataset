N=int(input())
S = input()

W=[1 if S[0]=="." else 0]
ans=float("inf")

for i in range(1,N):
  if S[i]==".":
    W.append(W[-1]+1)
  else:
    W.append(W[-1])
    
if W[-1]==0 or W[-1]==N:
  print(0)
  exit()

for i in range(N):
  cost_W = i+1-W[i]
  cost_B = W[-1]-W[i]
  cost=cost_W+cost_B
  #print(N, W[-1], i+1, W[i])
  #print(i,"cost_W:",cost_W,"cost_B:",cost_B,"Total",cost)
  ans=min(ans,cost)
ans=min(W[-1],N-W[-1],ans)
print(ans)