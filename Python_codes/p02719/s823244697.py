N, K = map(int, input().split())
res = N % K
if abs(K-res) < res:
  res = abs(K-res)
print(res)