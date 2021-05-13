N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
  XY[i] = [XY[i][0] - XY[i][1], XY[i][0] + XY[i][1]]
X = [XY[i][0] for i in range(N)]
Y = [XY[i][1] for i in range(N)]
X.sort()
Y.sort()
print(max(X[-1] - X[0], Y[-1] - Y[0]))