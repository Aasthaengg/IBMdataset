import math
A, B, C, D, E, F = map(int, input().split())

def calc(a, b):
    if a == 0 or b == 0: return 0
    return 100 * b / (a + b)
ans = (0, 0)
tmp = 0
ret = set()
for i in range(3001):
    for j in range(3001):
        water = i * A * 100 + j * B * 100
        if 1 > water or water > F: break
        for k in range((F-water)//C+1):
            for l in range((F-water)//D+1):
                suger = k * C + l * D
                if water + suger > F: break
                if water * E // 100 < suger: break
                t = calc(water, suger)
                #ret.add((t, water+suger, suger))
                if tmp <= t:
                    tmp = t
                    ans = (water+suger, suger)

#ret = list(ret)
#ret.sort(reverse=True)
print(*ans)
