"""
lazyseg使う方法とかもあるが、imos法使うのが簡単そう。
座標圧縮は必須。
"""
from math import ceil
N,D,A = map(int,input().split())
XH = [list(map(int,input().split())) for _ in range(N)]
XH.sort()

coordinates = set()
for x,h in XH:
    coordinates.add(x)
    coordinates.add(x+2*D+1)

compress = {x:i for i,x in enumerate(sorted(coordinates))}

imos = [0]*(len(compress))
damage = 0
cur = 0
ans = 0
for x,h in XH:
    compX = compress[x]
    while cur <= compX:
        damage += imos[cur]
        cur += 1
    rest = h-damage
    if rest > 0:
        add = A*ceil(rest/A)
        ans += int(ceil(rest/A))
        imos[cur] += add
        right = compress[x+2*D+1]
        imos[right] -= add
print(ans)