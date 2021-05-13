n = int(input())
TA = [list(map(int, input().split())) for _ in range(n)]

# from math import ceil

res = [1, 1]
for i in range(n):
    t, a = TA[i]
    # mx = max(ceil(res[0] / t), ceil(res[1] / a))
    mx = max(-(-res[0] // t), -(-res[1] // a))
    res = [t * mx, a * mx]

print(sum(res))