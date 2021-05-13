W, H, N = map(int, input().split())
R = [list(map(int, input().split())) for _ in range(N)]
X,Y = [0, W],[0, H]
for r in R:
  if r[2]==1:
    X[0] = max(X[0], r[0])
  elif r[2]==2:
    X[1] = min(X[1], r[0])
  elif r[2]==3:
    Y[0] = max(Y[0], r[1])
  else:
    Y[1] = min(Y[1], r[1])
print(max(0, (X[1]-X[0]))*max(0, (Y[1]-Y[0])))