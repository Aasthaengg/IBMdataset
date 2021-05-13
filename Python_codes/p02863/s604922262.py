N,T=map(int,input().split())
L=[]
for i in range(N):
  a,b=map(int,input().split())
  L.append((a,b))
L.sort()

DP=[[0 for i in range(T)] for j in range(N)]

for i in range(N):
  a=L[i][0]
  b=L[i][1]
  for j in range(min(T,a)):
    DP[i][j]=DP[i-1][j]
  for j in range(min(T,a),T):
    DP[i][j]=max(DP[i-1][j-a]+b,DP[i-1][j])
    
ans=0
for i in range(N-1):
  ans=max(ans,DP[i][T-1]+L[i+1][1])
print(ans)