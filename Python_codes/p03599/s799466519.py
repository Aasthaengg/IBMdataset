from itertools import product
from collections import namedtuple
A, B, C, D, E, F = map(int, input().split())

r100 = lambda x: range(F//(100*x)+1)
cct = 0
sw = namedtuple('sw', ['suger', 'water']) #suger_water
ans = sw(0, A*100)
for a, b in product(r100(A), r100(B)):
    water = (a * A + b * B) * 100
    if water > F or water == 0:
        continue
    r = lambda x: range((F-water)//x+1)
    for c, d in product(r(C), r(D)):
        suger = c * C + d * D
        if  water + suger > F:
            continue

        if suger * 100 > water * E:
            continue
        
        if water+suger == 0:
            continue

        if cct < 100 * suger/(suger+water):
            cct = 100 * suger/(suger+water)
            ans = sw(suger, water)

print(ans.suger+ans.water, ans.suger)