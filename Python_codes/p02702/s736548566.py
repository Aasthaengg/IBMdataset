import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(map(int, list(input())))
mod = 2019
lens = len(S)
mods = [0]*lens
cum = 0
for i in range(lens):
    s = S[-i-1]
    cum += s*pow(10, i, mod)
    cum %= mod
    mods[i] = cum
mods += [0]
from collections import Counter
c = Counter(mods)

ans = 0
for num, cnt in c.most_common():
    if cnt<2:
        break
    ans += cnt*(cnt-1)//2
print(ans)