# -*- coding: utf-8 -*-
import sys
from itertools import accumulate 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,W = map(int,readline().split())
A1 = []
A2 = []
A3 = []
A4 = []
w1,v1 = map(int,readline().split())
A1.append(v1)

for _ in range(N-1):
    w,v = map(int,readline().split())
    if w == w1:
        A1.append(v)
    elif w == w1+1:
        A2.append(v)
    elif w == w1+2:
        A3.append(v)
    else:
        A4.append(v)

S1 = list(accumulate(sorted(A1,reverse = True)))
S2 = list(accumulate(sorted(A2,reverse = True)))
S3 = list(accumulate(sorted(A3,reverse = True)))
S4 = list(accumulate(sorted(A4,reverse = True)))

S1 = [0] + S1
S2 = [0] + S2
S3 = [0] + S3
S4 = [0] + S4

ans = 0
for a in range(len(S1)):
    for b in range(len(S2)):
        for c in range(len(S3)):
            for d in range(len(S4)):
                tmp = w1*(a+b+c+d)+b+2*c+3*d
                total = S1[a]+S2[b]+S3[c]+S4[d]
                if tmp <= W:
                    ans = max(ans,total)
print(ans)