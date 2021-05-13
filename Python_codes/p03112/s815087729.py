import sys
input = sys.stdin.readline
from bisect import bisect

A,B,Q = map(int,input().split())
S = [int(input()) for i in range(A)]
T = [int(input()) for i in range(B)]
X = [int(input()) for i in range(Q)]

INF = float('inf')
st = []
for s in S:
    i = bisect(T,s)
    x0,x1 = -INF,INF
    if i > 0: x0 = T[i-1]
    if i < B: x1 = T[i]
    st.append(min(s-x0, x1-s))
ts = []
for t in T:
    i = bisect(S,t)
    x0,x1 = -INF,INF
    if i > 0: x0 = S[i-1]
    if i < A: x1 = S[i]
    ts.append(min(t-x0, x1-t))

ans = []
for x in X:
    d0 = d1 = d2 = d3 = INF
    si = bisect(S,x)
    if si > 0:
        d0 = x-S[si-1] + st[si-1]
    if si < A:
        d1 = S[si]-x + st[si]
    ti = bisect(T,x)
    if ti > 0:
        d2 = x-T[ti-1] + ts[ti-1]
    if ti < B:
        d3 = T[ti]-x + ts[ti]
    ans.append(min(d0,d1,d2,d3))
print(*ans, sep='\n')