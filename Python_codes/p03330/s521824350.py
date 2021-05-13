INF = float('inf')
N, C = map(int, input().split())
D = list() #D[i][j]:=iからjに変える時の違和感
graph = list()
for i in range(C):
  D.append(list(map(int, input().split())))
for i in range(N):
  graph.append(list(map(int, input().split())))
E = [[0] * C for _ in range(3)] #E[i][j]:=mod3でiの場所を全て色jにしたときの違和感
for c in range(C):
  for x in range(N):
    for y in range(N):
      p = (x+y+2)%3
      cxy = graph[x][y]-1
      E[p][c] += D[cxy][c]
F = [[[INF]*2 for _ in range(3)] for _ in range(3)] 
#F[i][j][k]:=mod3でiの場所の違和感の最小値第j+1位。k=0色番号, k=1最小値]
for i in range(3):
  for j in range(C):
    if(E[i][j] < F[i][0][1]):
      F[i][2] = F[i][1]
      F[i][1] = F[i][0]
      F[i][0] = [j, E[i][j]]
    elif(E[i][j] < F[i][1][1]):
      F[i][2] = F[i][1]
      F[i][1] = [j, E[i][j]]
    elif(E[i][j] < F[i][2][1]):
      F[i][2] = [j, E[i][j]]
      
ans = INF
for i in range(3):
  for j in range(3):
    for k in range(3):
      c0 = F[0][i][0]
      c1 = F[1][j][0]
      c2 = F[2][k][0]
      if(c0 != c1 and c1 != c2 and c2 != c0):
        ans = min(ans, F[0][i][1]+F[1][j][1]+F[2][k][1])
print(ans)