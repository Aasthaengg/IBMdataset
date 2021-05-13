n,m = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(m)]
p = list(map(int,input().split()))

from itertools import product

ans = 0
for a in product([0,1],repeat=n):
    for j,l in enumerate(li):
        t = 0
        for k in l[1:]:
            t += a[k-1]
        t %= 2
        if t != p[j]:break
    else:
        ans += 1

print(ans)