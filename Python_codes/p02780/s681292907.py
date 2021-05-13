N, K, *X = map(int, open(0).read().split())

y = [float(x * (x + 1) / 2 / x) for x in X]
ans = sum(y[:K])
res = ans
for i in range(K, N):
    res = res - y[i - K] + y[i]
    ans = max(ans, res)
print(ans)
