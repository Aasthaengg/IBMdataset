from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [0] * (N + 1)
for i in range(N):
    X[i + 1] = X[i] + A[i] % M
    X[i + 1] %= M
X = X[1:]
d = defaultdict(int)
for x in X:
    d[x] += 1
ans = d[0]
for k, v in d.items():
    if 2 <= v:
        ans += v * (v - 1) // 2
print(ans)