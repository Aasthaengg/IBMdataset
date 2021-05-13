N, K, S = map(int, input().split())
ans = [0] * N

for i in range(K):
  ans[i] = S
for j in range(N - K):
  if S != 10 ** 9:
    ans[K + j] = S + 1
  else:
    ans[K + j] = 1
  
for i in range(N):
  print(ans[i], end = " ")