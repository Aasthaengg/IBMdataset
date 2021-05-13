N = int(input())
X = list(map(int,input().split()))
X.sort()
ans = float("INF")
for i in range(X[0], X[-1] + 1):
  count = 0
  for j in X:
    count += (j - i) ** 2
  ans = min(ans, count)
print(ans)