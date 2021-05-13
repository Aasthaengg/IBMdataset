N = int(input())
A = list(map(int, input().split(' ')))
a = 0
for i in range(N):
  a += (-1) ** i * A[i]
res = [0 for _ in range(N)]
res[0] = a
print('{} '.format(res[0]), end='')
for i in range(1, N - 1):
  res[i] = 2 * A[i-1] - res[i-1]
  print('{} '.format(res[i]), end='')
res[N-1] = 2 * A[N-2] - res[N-2]
print(res[N-1])