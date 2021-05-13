
from collections import defaultdict

N, K = map(int, input().split())
X = list(map(int, input().split()))

cs = [0] * (N + 1)
for i in range(N):
    cs[i + 1] = cs[i] + X[i]

y = [(cs[i] - i) % K for i in range(N + 1)]
ctr = defaultdict(int)
ans = 0
for i in range(N + 1):
    ans += ctr[y[i]]
    ctr[y[i]] += 1
    if i - K + 1 >= 0:
        ctr[y[i - K + 1]] -= 1

print(ans)
