def solve():
  N, K = map(int, input().split())
  if K > (N - 1) * (N - 2) // 2:
    print(-1)
    return
  else:
    root = [[False for _ in range(N + 10)] for _ in range(N + 10)]
    M = (N - 1) * (N - 2) // 2 - K
    i = 1
    j = 2
    print(M + N - 1)
    for k in range(N - 1):
      print('1 {}'.format(k + 2))
    for _ in range(M):
      print('{0} {1}'.format(i + 1, j + 1))
      j += 1
      if j == N:
        i += 1
        j = i + 1
    return
solve()