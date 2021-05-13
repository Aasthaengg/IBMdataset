from math import gcd
from collections import defaultdict

n,m = map(int,input().split())
s = input()
t = input()

ans = n*m // gcd(n,m)
d = defaultdict(lambda : '?')

for i,si in enumerate(s):
    d[i * ans//n] = si

for j,tj in enumerate(t):
    if(not d[j * ans//m] in ['?', tj]):
        print(-1)
        exit()

print(ans)