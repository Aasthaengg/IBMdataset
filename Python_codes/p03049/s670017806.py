#!/usr/bin/env python3

N = int(input())
S = [input() for i in range(N)]

ret = 0

for s in S:
    ret += s.count('AB')

D = [0] * N
for i in range(N):
    r = [0, 0]
    if S[i][0] == 'B':
        r[0] = 1
    if S[i][-1] == 'A':
        r[1] = 1

    D[i] = r

b_c = D.count([1, 0])
a_c = D.count([0, 1])
ab_c = D.count([1, 1])

if ab_c == 0:
    ret += min(b_c, a_c)
else:
    if a_c + b_c > 0:
        ret += ab_c + min(a_c, b_c)
    else:
        ret += ab_c - 1


print(ret)
