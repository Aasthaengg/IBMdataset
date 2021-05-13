N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

XY.sort()
#print("XY:", XY)

answer = []
for i in range(N):
  for k in range(K, N + 1):
    if i + k - 1 >= N:
      break
    dx = XY[i + k - 1][0] - XY[i][0]
    Y = []
    for x, y in XY[i: i + k]:
      Y.append(y)
    Y.sort()
    lenY = len(Y)
    for j in range(k):
      if j + K - 1 == lenY:
        break
      dy = Y[j + K - 1] - Y[j]
      answer.append(dx * dy)

print(min(answer))