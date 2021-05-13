n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [0]
for i in range(1, n):
  tmp = float('inf')
  for j in range(k):
    if i-j > 0:
      tmp = min(tmp, dp[-1-j]+abs(h[i]-h[i-1-j]))
  dp.append(tmp)
print(dp[-1])