n,m,Q = map(int,input().split())
lr = [list(map(int,input().split())) for _ in range(m)]
lr.sort(key=lambda x:(x[0],x[1]))
ans = [[0]*(n+1) for _ in range(n+1)]
now = 0
for i in range(1,n+1):
  j = 1
  while True:
    if now < m:
      if lr[now][1] == j and lr[now][0] == i:
        ans[i][j] += (ans[i][j]==0)*(ans[i][j-1]) + 1
        now += 1
      else:
        j += 1
        if j <= n:
          ans[i][j] = ans[i][j-1]
        else:
          break
    else:
      j += 1
      if j <= n:
        ans[i][j] = ans[i][j-1]
      else:
        break
ans2 = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
  for j in range(1,n+1):
    if i == 1:
      ans2[i][j] = ans[i][j]
    else:
      ans2[i][j] = ans2[i-1][j] + ans[i][j]
for i in range(Q):
  p,q = map(int,input().split())
  print(ans2[q][q]-ans2[p-1][q])