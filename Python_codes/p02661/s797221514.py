n = int(input().strip())
ab = [tuple(map(int, input().split())) for _ in range(n)]

mid_min = 0
mid_max = 0

ab.sort(key=lambda x: x[0])
if n & 1:
    mid_min = ab[n // 2][0]
else:
    mid_min = (ab[(n - 1) // 2][0] + ab[n // 2][0])

ab.sort(key=lambda x: x[1])
if n & 1:
    mid_max = ab[n // 2][1]
else:
    mid_max = (ab[(n - 1) // 2][1] + ab[n // 2][1])

print(mid_max - mid_min + 1)
