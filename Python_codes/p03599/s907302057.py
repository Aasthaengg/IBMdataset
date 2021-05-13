import math

a, b, c, d, e, f = map(int, input().split())

highest = 0
sugarwater = 0
maxsugar = 0
amax = math.ceil(f / (100 * a))
bmax = math.ceil(f / (100 * b))
cmax = math.ceil(30 * e / c)
dmax = math.ceil(30 * e / d)
for aa in range(amax):
    for bb in range(bmax):
        water = 100 * (aa * a + bb * b)
        if water == 0 or water > f:
            continue
        for cc in range(cmax):
            for dd in range(dmax):
                sugar = cc * c + dd * d
                if sugar / (water / 100) > e or water + sugar > f:
                    continue
                density = 100 * sugar / (water + sugar)
                if density >= highest:
                    highest = density
                    sugarwater = sugar + water
                    maxsugar = sugar
print(sugarwater, maxsugar)
