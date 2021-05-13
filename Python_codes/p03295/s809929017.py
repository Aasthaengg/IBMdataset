n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ab.sort(key=lambda x: x[0])

c_l = 0
c_r = n+1

res = 0
for i, v in enumerate(ab):
    a, b = v
    if c_r <= a:
        res += 1
        c_l = a
        c_r = b
    else:
        c_l = max(c_l, a)
        c_r = min(c_r, b)

print(res+1)