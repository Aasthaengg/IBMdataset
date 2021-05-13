from math import gcd
from collections import defaultdict

N, M = map(int, input().split())
S = input()
T = input()
g = N//gcd(N, M)*M
ans = defaultdict(bool)
for i in range(N):
    ans[i*g//N] = S[i]
ok = True
for i in range(M):
    idx = i*g//M
    if ans[idx] and ans[idx] != T[i]:
        ok = False
        break
if ok:
    print(g)
else:
    print(-1)
