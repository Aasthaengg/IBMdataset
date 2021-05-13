from itertools import accumulate

n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
acc = [0] + list(accumulate(v))
for l in range(min(n, k) + 1):
    for r in range(min(n, k) - l + 1):
        minus = sorted(v[:l] + v[n - r:])
        bag = acc[l] - acc[0] + acc[n] - acc[n - r]
        bag -= sum(vi for vi in minus[:k - l - r] if vi < 0)
        ans = max(ans, bag)
print(ans)
