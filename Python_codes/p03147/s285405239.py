n = int(input())
h = list(map(int, input().split()))
ans = 0
for k in range(100, 0, -1):
    ans += sum(hi == k for hi in h)
    ans -= sum(hi == hj == k for hi, hj in zip(h, h[1:]))
    h = list(map(lambda x: min(x, k - 1), h))
print(ans)
