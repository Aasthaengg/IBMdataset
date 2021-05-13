from collections import defaultdict
from sys import stdin
input = stdin.readline
d = defaultdict(int)
n,k = map(int,input().split())
for _ in range(n):
    a,b = map(int,input().split())
    d[a]+=b
for key in sorted(d.keys()):
    v = d[key]
    k-=v
    if k <= 0:
        break
print(key)