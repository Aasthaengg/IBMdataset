N, K = map(int, input().split())
def getCombinationCount(N, K):
  if N == 1:
    return K
  else:
    return K * (K - 1) ** (N - 1)

print(getCombinationCount(N, K))