N = int(input())
S = [input() for i in range(N)]
from collections import Counter
ctr = Counter([s[0] for s in S])

ans = 0
import itertools
for ptn in itertools.combinations('MARCH',3):
    a,b,c = ptn
    ans += ctr[a] * ctr[b] * ctr[c]
print(ans)