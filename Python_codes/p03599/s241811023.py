a, b, c, d, e, f = map(int, input().split())

memo = {}

for x in range(31):
    for y in range(31):
        for s in range(101):
            for t in range(101):
                water = (100*a)*x + (100*b)*y
                sugar = s*c + t*d
                if water == 0:
                    break
                if water + sugar > f:
                    break
                else:
                    if water/100 * e >= sugar:
                        density = 100*sugar/(water + sugar)
                        memo[x, y, s, t] = density

max_v = max(memo.values())

for k, v in memo.items():
    if v == max_v:
        print((100*a)*k[0] + (100*b)*k[1] + c*k[2] + d*k[3], c*k[2] + d*k[3])
        break
