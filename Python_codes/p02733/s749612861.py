def main():
    #import numpy as np
    import sys, math
    from itertools import permutations, combinations
    from collections import defaultdict, Counter, deque
    from math import factorial#, gcd
    from bisect import bisect_left #bisect_left(list, value)
    sys.setrecursionlimit(10**7)
    enu = enumerate
    MOD = 10**9+7
    def input(): return sys.stdin.readline()[:-1]
    pl = lambda x: print(*x, sep='\n')

    H, W, K = map(int, input().split())
    S = [list(map(int, list(input()))) for _ in range(H)]

    from copy import deepcopy
    cS = [[0]*(W+1) for _ in range(H+1)]
    # cS = deepcopy(S)

    for h in range(1, H+1):
        for w in range(W):
            cS[h][w+1] = cS[h][w] + S[h-1][w]
    for w in range(1, W+1):
        for h in range(H):
            cS[h+1][w] = cS[h][w] + cS[h+1][w]
    # pl(cS)

    mcut = 10**9
    for i in range(2**(H-1)):
        yoko = []
        for j in range(H):
            if ((i >> j) & 1):
                yoko.append(j+1)
        yoko = [0] + yoko + [H]
        # yoko.append(H)
        # print(yoko)
        
        cut = len(yoko)-2
        lastcut = 0 # index-w
        w = 1
        cannot = False
        while w < W+1:
            if cannot:
                w = W + 100
                break
            for ind, y in enu(yoko):
                if ind == 0:
                    continue
                v1 = cS[y][w]
                v2 = cS[yoko[ind-1]][w]
                v3 = cS[yoko[ind-1]][lastcut]
                v4 = cS[y][lastcut]
                val = v1 - v2 + v3 - v4
                # print('  v1, v2', v1, v2)
                if K < val:
                    cut += 1
                    if lastcut == w-1:
                        cannot = True
                    lastcut = w-1
                    break
            else:
                w += 1
            # print(' val', val)
        if not(cannot) and cut < mcut:
            # print('yoko', yoko)
            mcut = cut

    print(mcut)
if __name__ == '__main__':
    main()