N,K=map(int,input().split())
nodes=[]
for i in range(N):
  x,y=map(int,input().split())
  nodes.append((x,y))
nodes.sort()
import math
ans=math.inf
count=0
for i in range(N):
  for j in range(i+1,N):
    for k in range(N):
      for l in range(i+1,N):
        count=0
        for m in range(N):
          small=min(nodes[k][1],nodes[l][1])
          big=max(nodes[k][1],nodes[l][1])
          if nodes[i][0]<=nodes[m][0]<=nodes[j][0] and small<=nodes[m][1]<=big:
            count+=1
        if count>=K:
          ans=min(ans,(nodes[j][0]-nodes[i][0])*(big-small))
print(ans)