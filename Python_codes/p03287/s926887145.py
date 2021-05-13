import collections
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 普通の累積和
cumsum = [0]
for i in range(N):
    cumsum.append(cumsum[-1] + A[i])

# 上で作った累積和のmodMを計算
cumsum_mod = []
for i in range(N + 1):
    cumsum_mod.append(cumsum[i] % M)

c = collections.Counter(cumsum_mod)

ans = 0
for v in c.values():
    ans += v * (v - 1) // 2

print(ans)
