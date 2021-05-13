(n,),*axy = [list(map(int, s.split())) for s in open(0)]

from itertools import product
from collections import defaultdict
d = defaultdict(defaultdict)

i = 0
for elm in axy:
    if len(elm) == 1:
        i += 1
    else:
        x,y = elm
        d[i][x] = y
del i

ans = 0
for flgs in product([0,1], repeat=n):
    honest = [i for i, v in zip(range(1, n+1), flgs) if v]
    valid = True
    for i in honest:
        if not valid:
            break
        if not i in d:
            continue
        for j in d[i]:
            if (j in honest and not d[i][j]) or (j not in honest and d[i][j]):
                valid = False
                break
    if valid:
        ans = max(ans, len(honest))

print(ans)