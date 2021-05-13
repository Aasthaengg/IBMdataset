N, X, Y = map(int, input().split())
distcnt = [0] * (N-1)
for i in range(1, N):
  for j in range(i+1, N+1):
    disttmp = min(j-i, abs(X-i) + 1 + abs(j-Y))
    distcnt[disttmp-1] += 1
for i in range(N-1):
  print(distcnt[i])
