from itertools import accumulate
from collections import defaultdict
n,m = map(int, input().split())
As = list(map(int, input().split()))
acc = list(accumulate([0]+As))
amari = [a%m for a in acc]


# あまりが0になるものを抜粋していく
d = defaultdict(int)
for a in amari:
    d[a] += 1
ans = 0
for k in d.keys():
    x = d[k]
    ans += x*(x-1)//2
print(ans)