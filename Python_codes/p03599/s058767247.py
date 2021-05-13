from copy import deepcopy
import itertools

A, B, C, D, E, F = map(int, input().split())

qA = [i // 100 for i in range(0, F + 1, A * 100)]
qB = [i // 100 for i in range(0, F + 1, B * 100)]
qC = [i for i in range(0, F + 1, C)]
qD = [i for i in range(0, F + 1, D)]

W = set(qA + qB)
for i in range(F // min(A, B)):
    nW = deepcopy(W)
    for w in W:
        if (w + A) * 100 <= F:
            nW.add(w + A)
        if (w + B) * 100 <= F:
            nW.add(w + B)

    if len(W) == len(nW):
        break
    W = deepcopy(nW)

W = nW

S = set(qC + qD)
for i in range(F // min(C, D)):
    nS = deepcopy(S)
    for s in S:
        if (s + C) <= F:
            nS.add(s + C)
        if (s + D) <= F:
            nS.add(s + D)

    if len(S) == len(nS):
        break
    S = deepcopy(nS)
S = nS

M = 0
Ms = 0
Mw = A
for w, s in itertools.product(W, S):
    if w != 0 and s <= w * E and s + 100 * w <= F:
        if M < s / (w * 100 + s):
            M = s / (w * 100 + s)
            Ms = s
            Mw = w

print(Ms + Mw * 100)
print(Ms)
