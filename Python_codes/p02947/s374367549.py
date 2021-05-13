import sys
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()

N = I()
s = [''.join(sorted(S())) for i in range(N)]

from collections import Counter

c = Counter(s)
ans = 0
for i in c.keys():
    ans += c[i]*(c[i]-1)//2

print(ans)
