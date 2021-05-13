import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

from collections import defaultdict
import math
n,m = map(int, input().split())
s = input()
t = input()
g = math.gcd(n,m)
d = defaultdict(list)
for i in range(n):
    ind = i*(m//g)
    d[ind].append(s[i])
for i in range(m):
    ind = i*(n//g)
    d[ind].append(t[i])
for k,v in d.items():
    if v and not all(item==v[0] for item in v):
        ans = -1
        break
else:
    ans = n*m//g
print(ans)
