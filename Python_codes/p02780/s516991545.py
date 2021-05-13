
N, K = map(int, input().split())
X = list(map(int, input().split()))

cur = sum((X[i] + 1) / 2 for i in range(K))
ans = cur
for i in range(K, N):
    cur += (X[i] + 1) / 2 - (X[i - K] + 1) / 2
    ans = max(ans, cur)

print(ans)
