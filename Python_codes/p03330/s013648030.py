#然列挙では間に合わない
N,C = map(int,input().split())
ld = [[]]
for i in range(C):
  ld.append([0]+list(map(int,input().split())))
lc = [[]]  
for i in range(N):
  lc.append([0]+list(map(int,input().split())))

#前処理
lmae = [[0 for i in range(C+1)] for j in range(3)]
for p in range(1,N+1):
  for q in range(1,N+1):
    for i in range(1,C+1):
      X = lc[p][q]
      Y = i
      lmae[(p+q)%3][i] += ld[X][Y]

#こたえ作り
lans = []
for i in range(1,C+1):
  for j in range(i+1,C+1):
    for k in range(j+1,C+1):
      for cc in [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]:
        ans = lmae[cc[0]][i]+lmae[cc[1]][j]+lmae[cc[2]][k]
        lans.append(ans)
print(min(lans))      