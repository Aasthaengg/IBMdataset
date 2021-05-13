#!python3

from time import perf_counter
limit = 1.91
tick = perf_counter()

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())
from random import randrange

def resolve():
    G = 26
    it = map(int, sys.stdin.read().split())
    D = next(it)
    C = [next(it) for i in range(G)]
    S = [[next(it) for i in range(G)] for i in range(D)]
    T = [0] * D
    L = [-1] * 26

    U = 7
    def calc(i, j):
        score = S[i][j]
        for k in range(G):
            u = k - L[k]
            score -= C[k] * (u + u + U) * U // 2
        score += C[k] * U * (i-L[j])
        return score

    def fullscore():
        score = 0
        last = [-1] * G
        rate = [0] * G
        for i, ti in enumerate(T):
            score += S[i][ti]
            x = i - last[ti]
            rate[ti] += x * (x-1) // 2
            last[ti] = i

        for i, (l, r) in enumerate(zip(last, rate)):
            x = D - l
            x = x * (x-1) // 2
            score -= C[i] * (r + x)

        return score

    for di in range(D):
        i, score = 0, calc(di, 0)
        for qi in range(1, G):
            x = calc(di, qi)
            if x > score:
                i, score = qi, x
        L[i] = di
        T[di] = i

    t = num = 0
    #s0 = fullscore()
    back_t = dict()
    #from collections import defaultdict; CC = defaultdict(int); CC2 = defaultdict(int)
    while t < limit:
        ab = randrange(0, 100)
        if ab > 50:
            di, qi = randrange(0, D), randrange(0, G)

            if not di in back_t:
                back_t[di] = T[di]
            T[di] = qi
        else:
            di = randrange(0, D-1)
            dj = randrange(di+1, D)

            for i in (di, dj):
                if not i in back_t:
                    back_t[i] = T[i]

            T[di], T[dj] = T[dj], T[di]

        sc = fullscore()
        t = perf_counter() - tick
        rate = t / limit
        if sc > score:
            score = sc
            back_t = dict()

            #CC[num] += 1
            #num = 0
        elif rate * score > sc:
            for k, v in back_t.items():
                T[k] = v
            #CC2[num] += 1
            back_t = dict()
            #num = 0
        else:
            #num += 1
            pass


    for k, v in back_t.items():
        T[k] = v

    print(*(i+1 for i in T), sep="\n")
    #print(s0, score, fullscore());print(*CC.items());print(*CC2.items())

if __name__ == "__main__":
    resolve()
