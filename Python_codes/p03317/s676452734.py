N, K = map(int, input().split())
A = list(map(int, input().split()))
t = A.index(1)
ans = 10 ** 7
for i in range(K):
    pre = max(t + i, 0)
    tail = max(N - 1 - t - i, 0)
    unit = K - 1
    pre_unit = -(-pre // unit)
    tail_unit = -(-tail // unit)
    ans = min(ans, pre_unit + tail_unit)
print(ans)
