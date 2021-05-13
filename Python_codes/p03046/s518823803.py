M, K = map(int, input().split())
if K > 2 ** M - 1:
  print(-1)
elif M == 1 and K == 0:
  print('0 0 1 1')
elif M == 1 and K == 1:
  print(-1)
else:
  ans = [i for i in range(2 ** M) if i != K] + [K] + [i for i in range(2 ** M - 1, -1, -1) if i != K] + [K]
  print(' '.join(map(str, ans)))