H,W = map(int,input().split())
A = []
for i in range(H):
  temp = list(map(int,input().split()))
  A.append(temp)
#print(A)
ans = 0
L = []
for i in range(H):
  for j in range(W):
    if A[i][j]%2 == 1:#奇数なら動かす
      if j <= W-2 and A[i][j+1]%2 == 1: #右が奇数
        ans +=1
        A[i][j] -=1
        A[i][j+1] +=1
        L.append([i,j,i,j+1])
      elif i <= H-2 and A[i+1][j]%2 == 1: #下が奇数
        ans +=1
        A[i][j]-=1
        A[i+1][j] += 1
        L.append([i,j,i+1,j])
      else: #どちらも偶数
        if j <=W-2: #横に動かす
          ans +=1
          A[i][j] -=1
          A[i][j+1] +=1
          L.append([i,j,i,j+1])
        elif i <= H-2: #下に動かす
          ans +=1
          A[i][j]-=1
          A[i+1][j] += 1
          L.append([i,j,i+1,j])
print(ans)
for t in L:
  temp = []
  for x in t:
    temp.append(x+1)
  print(*temp)