import sys
input = sys.stdin.readline
from bisect import bisect_left
inf = float('inf')

N, Q = map(int,input().split())
STX = [list(map(int,input().split())) for _ in range(N)]
D = [int(input()) for _ in range(Q)]

res = 1
while res < Q:
    res <<= 1
N0 = res
data = [inf for _ in range(2*N0-1)]

def update(l, r, x):
    L = l + N0
    R = r + N0
    while L < R:
        if R & 1:
            R -= 1
            data[R] = min(data[R], x)
        if L & 1:
            data[L] = min(data[L], x)
            L += 1
        L >>= 1; R >>= 1

def value(k):
    k += N0
    res = data[k]
    while k != 0:
        k >>= 1
        res = min(res, data[k])
    return res


for S, T, X in STX:
    l = bisect_left(D, S-X)
    r = bisect_left(D, T-X)
    update(l, r, X)

for k in range(Q):
    ans = value(k)
    if ans == inf:
        ans = -1
    print(ans)