from bisect import bisect_left
n, k = map(int, input().split())
candles = list(map(int, input().split()))
point_zero = bisect_left(candles, 0)
candles.insert(point_zero, 0)
ans = float('inf')
for i in range(min(k, point_zero) + 1):
    left = point_zero - i
    right = point_zero + k - i
    if (0 <= left) and (right < n + 1):
        dis = -candles[left] + candles[right] + min(-candles[left], candles[right])
        ans = min(ans, dis)
print(ans)