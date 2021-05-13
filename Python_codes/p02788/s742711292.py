#  --*-coding:utf-8-*--

import math

N,D,A = map(int, input().split())
XH = sorted(tuple(map(int, input().split())) for _ in range(N))

Q = []
qIdx = 0
s = 0
t = 0

for (x, h) in XH:
    while qIdx < len(Q) and  Q[qIdx][0] < x:
        s -= Q[qIdx][1]
        qIdx += 1

    if s < h:
        q = int(math.ceil((h-s)/A))
        Q.append((x+2*D, q*A))
        s += q*A
        t += q

print(t)
