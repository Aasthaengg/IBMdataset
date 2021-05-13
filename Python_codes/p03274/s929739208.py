import bisect

N, K = [int(i) for i in input().split()]
candles = [int(i) for i in input().split()]

if 0 not in candles:
    zero_index = bisect.bisect(candles, 0)
else :
    zero_index = candles.index(0)

start_index = max(0, zero_index-K)
end_index = min(start_index+K, N-K+1)

distances = []
for i in range(start_index, end_index):
    if candles[i] < 0 and 0 < candles[i+K-1]:
        dist_left = abs(candles[i])
        dist_right = candles[i+K-1]
        dist = (2 * min(dist_left, dist_right)) + max(dist_left,dist_right)
    else :
        dist = max(abs(candles[i]), abs(candles[i+K-1]))
    distances.append(dist)

print(min(distances))