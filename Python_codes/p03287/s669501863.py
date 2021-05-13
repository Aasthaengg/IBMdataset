import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
As = [0]+list(mapint())
from itertools import accumulate
cAs = list(accumulate(As))

for i in range(N+1):
    cAs[i] = cAs[i]%M

from collections import Counter
c = Counter(cAs)
ans = 0
for num, cnt in c.most_common():
    if cnt<2:
        break
    ans += cnt*(cnt-1)//2

print(ans)