N,K = map(int, input().split())
points = list(map(int,input().split()))
for n in range(N - K):
  print('Yes' if points[n] < points[n + K] else 'No')