def getValue(mid):
    return (mid // 2) * 6 + (mid // 2) * 5 + 6 * (bool(mid % 2))

n = int(input())
l, r = 1, 10 ** 15
result = float("inf")
while l <= r:
    mid = (l + r) // 2
    cur = getValue(mid)
    if cur >= n:
        result = mid
        r = mid - 1
    else:
        l = mid + 1
print(result)