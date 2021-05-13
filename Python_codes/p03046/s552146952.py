M, K = map(int, input().split())
if K >= (2 ** M):
  print(-1)
elif M == 0:
  print("0 0")
elif M == 1:
  if K == 0:
    print("0 0 1 1")
  else: print(-1)
else:
  print(" ".join(map(str, [i for i in range(2 ** M) if i != K] + [K] + [i for i in range(2 ** M - 1, -1 , -1) if i != K] + [K])))