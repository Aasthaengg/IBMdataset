import sys
from heapq import *
input = sys.stdin.readline
N, K = map(int, input().split())
D, H, var, res = [], [], set(), 0
for _ in range(N):
    t,d = map(int, input().split())
    D.append((t,d))
D.sort(key=lambda x: x[1], reverse=True)
for t, d in D[:K]:
    if t not in var: var.add(t)
    else: heappush(H, d)
    res += d
x = len(var)
res += x**2
tmp = res
for t, d in D[K:]:
    if H and t not in var:
        tmp += d-heappop(H)+2*x+1
        x += 1
        var.add(t)
        res = max(res,tmp)
print(res)