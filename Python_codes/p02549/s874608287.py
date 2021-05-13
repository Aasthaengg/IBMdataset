N, K = map(int, input().split())
L = []
R = []

mod = 998244353

for i in range(K):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r + 1)

diff = [0] + [1] + [-1] + [0] * (10 ** 5 * 5)
ans = [0] * (10 ** 5 * 5)

for i in range(1, N + 1):
    ans[i] = ans[i-1] + diff[i]
    ans[i] %= mod
    for j in range(K):
        diff[i + L[j]] += ans[i]
        diff[i + R[j]] -= ans[i]
        diff[i + L[j]] %= mod
        diff[i + R[j]] %= mod

print(ans[N])