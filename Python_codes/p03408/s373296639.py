import sys
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()

N = I()
s = [S() for i in range(N)]
M = I()
t = [S() for i in range(M)]

from collections import Counter

c1 = Counter(s)
c2 = Counter(t)
ans = 0
for a in c1.keys():
    ans = max(ans,c1[a]-c2[a])

print(ans)