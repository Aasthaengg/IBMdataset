N, M = list(map(lambda x: int(x), input().split(" ")))
ans = [0] * N
for i in range(M):
  a, b = list(map(lambda c: int(c), input().split(" ")))
  ans[a - 1] += 1
  ans[b - 1] += 1

print("\n".join([str(s) for s in ans]))