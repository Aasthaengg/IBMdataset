X, Y = map(int, input().split())
S = 0
R = [300000, 200000, 100000]
for i in range(max(X, Y)):
  R.append(0)

if X == 1 and Y == 1:
  print(R[X-1] + R[X-1] + 400000)
else:
  print(R[X-1] + R[Y-1])