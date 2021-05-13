k, a, b = map(int, input().split())
biscuits = 1
if a - 1 <= k:
    biscuits += a - 1
    k -= a - 1
if b - a > 3:
    biscuits += k // 2 * (b - a) + k % 2
else:
    biscuits += k
print(biscuits)
