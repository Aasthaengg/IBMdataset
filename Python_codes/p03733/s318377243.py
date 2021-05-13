N, T = [int(v) for v in input().split()]

res = 0
pre = -1e10
for t in [int(v) for v in input().split()]:
    res += T

    if pre + T > t:
        res -= (pre + T) - t
    pre = t

print(res)