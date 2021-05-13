from itertools import product
A,B,C,D,E,F=map(int, input().split())
ans = -float("inf")
mass = 0
sugarr = 0
for s, t in product(range(0, 31), repeat=2):
    water = 100*(A*s+B*t)
    if water > F or water == 0:
        continue
    up = min(F-water, E*(A*s+B*t))
    for u in range(0, up+1):
        if C*u > up:
            continue
        v = int((up-C*u)/D)
        if v < 0:
            continue
        sugar = C*u+D*v
        cons = sugar/(water+sugar)
        if cons > ans:
            ans = cons
            mass = water + sugar
            sugarr = sugar
print(mass, sugarr)