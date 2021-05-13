from collections import Counter
N,C=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(C)]
Grid=[[] for _ in range(3)]
for i in range(N):
  c=list(map(int,input().split()))
  for j in range(N):
    Grid[(i+j)%3].append(c[j])

for i in range(3):
  Grid[i]=Counter(Grid[i])

ans=float("inf")
for i in range(1,C+1):  
  for j in range(1,C+1):
    for k in range(1,C+1):
      if i!=j and j!=k and k!=i:
        an=0
        for g1 in Grid[0]:
          an+=D[g1-1][i-1]*Grid[0][g1]
        for g2 in Grid[1]:
          an+=D[g2-1][j-1]*Grid[1][g2]
        for g3 in Grid[2]:
          an+=D[g3-1][k-1]*Grid[2][g3]
        ans=min(ans,an)
        
print(ans)