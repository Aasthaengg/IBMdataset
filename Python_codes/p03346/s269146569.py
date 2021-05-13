N = int(input())
P = [int(input()) for _ in range(N)]

LIS = [0] * (N + 1)

for i in range(N):
  LIS[P[i]] = LIS[P[i] - 1] + 1
print(N - max(LIS))