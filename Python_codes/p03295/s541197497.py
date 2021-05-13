N,M=map(int,input().split())
BA=[]
for i in range(M):
  a,b=map(int,input().split())
  BA.append([b,a])
  
BA.sort()
ans=0
prev=-1
for i in range(M):
  if prev<=BA[i][1]:
    prev=BA[i][0]
    ans+=1
print(ans)