N, K = map(int, input().split())
h = list(map(int, input().split()))

costs = [0] * N

for i in range(1,N):
  minimum = 99999999999
  for j in range(1, min(K, i)+1):
    minimum = min(minimum, costs[i-j] + abs(h[i] - h[i-j]))
  costs[i] = minimum

print(costs[N-1])