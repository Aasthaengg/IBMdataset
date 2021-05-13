n, a,b,c = map(int, input().split())
l = [int(input()) for _ in range(n)]

import itertools
set123 = set([1,2,3])
ans = 10 ** 10
for i in itertools.product([0,1,2,3], repeat=n):
    if len(set(i) & set123) < 3:
        continue
    mp = 0
    ai = 0
    bi = 0
    ci = 0
    for j in range(n):
        if i[j] == 0:
            continue
        if i[j] == 1:
            if ai > 0:
                mp += 10
            ai += l[j]
        if i[j] == 2:
            if bi > 0:
                mp += 10
            bi += l[j]
        if i[j] == 3:
            if ci > 0:
                mp += 10
            ci += l[j]
    mp += abs(ai - a)
    mp += abs(bi - b)
    mp += abs(ci - c)
    ans = min(ans, mp)
print(ans)
