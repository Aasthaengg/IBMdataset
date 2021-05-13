import sys
from heapq import *
input = sys.stdin.readline
N, K = map(int, input().split())
D, H, var, res, L = [], [], set(), 0, N.bit_length()+2
for _ in range(N):
    t,d = map(int, input().split())
    D.append((d<<L)+t)
D.sort(reverse=True)
for z in D[:K]:
    d, t = z>>L, z%(1<<L)
    if t not in var: var.add(t)
    else: heappush(H, d)
    res += d
x = len(var)
res += x**2
tmp = res
for z in D[K:]:
    d, t = z>>L, z%(1<<L)
    if H and t not in var:
        tmp += d-heappop(H)+2*x+1
        x += 1
        var.add(t)
        res = max(res,tmp)
print(res)