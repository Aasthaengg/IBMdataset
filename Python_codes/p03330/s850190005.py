N, C=map(int, input().split())
D=[list(map(int, input().split())) for _ in range(C)]
c=[list(map(int, input().split())) for _ in range(N)]

grid=[[0]*C for _ in range(3)]

for i in range(N):
  for j in range(N):
    tmp=(i+j)%3
    
    for d in range(C):
      grid[tmp][d]+=D[c[i][j]-1][d]
      
print(min([grid[0][x]+grid[1][y]+grid[2][z] for x in range(C) for y in range(C) for z in range(C) if x!=y and y!=z and z!=x]))