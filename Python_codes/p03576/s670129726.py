N,K = map(int,input().split())

X = []
Y = []
Z = []

for i in range(N):
  x,y = map(int,input().split())
  X.append(x)
  Y.append(y)
  Z.append([x,y])
  
Y.sort()
X.sort()
ans = 10**100

for t in range(N):
  for u in range(N):
    for r in range(N):
      for l in range(N):
        T = Y[N-t-1]
        U = Y[u]
        R = X[N-r-1]
        L = X[l]
        
        if T <= U or R <= L:
          continue
        
        cnt = 0
        for i in range(N):
          xi = Z[i][0]
          yi = Z[i][1]
          if xi >= L and xi <= R and yi >= U and yi <= T:
            cnt += 1
        if cnt >= K:
          M = int( (T-U) * (R-L) )
          ans = min(ans,M)
          
print(ans)