from random import randint, getrandbits
import time
import sys
input = sys.stdin.readline
start = time.time()

def scoring():
    last = [0] * 26
    res = 0
    penalty = 0
    for i in range(D):
        t = out[i]
        res += S[i][t]
        penalty += sc - (i + 1 - last[t]) * C[t]
        res -= penalty
        last[t] = i + 1
    return res

D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]
out = [randint(0, 25) for _ in range(D)]
sc = sum(C)
score = scoring()
while time.time() < start + 1.80:
    if getrandbits(1):
        d = randint(0, D - 1)
        q = randint(0, 25)
        old = out[d]
        out[d] = q
        tmp = scoring()
        if tmp > score:
            score = tmp
        else:
            out[d] = old
    else:
        d1 = randint(0, D - 2)
        d2 = randint(d1 + 1, min(d1 + 16, D - 1))
        out[d1], out[d2] = out[d2], out[d1]
        tmp = scoring()
        if tmp > score:
            score = tmp
        else:
            out[d1], out[d2] = out[d2], out[d1]
for i in out:
    print(i + 1)