N=int(input())
X=[list(map(int,input().split())) for i in range(N)]
for i in range(N):
  X[i]=[X[i][0]+X[i][1],X[i][0]-X[i][1]]
print(max([max([X[i][j] for i in range(N)])-min([X[i][j] for i in range(N)]) for j in range(2)]))