#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

def solve(h, w, k, S):
    ret = float('inf')
    bits = 2 ** (h - 1)
    for b in range(bits):
        tmp = 0
        idx = 0
        groups = []
        for y in range(h):
            groups.append(idx)
            if (1 << y) & b:
                idx += 1
        m = idx + 1
        counts = [[0] * w for _ in range(m)]
        imp = False
        for y in range(h):
            g = groups[y]
            for x in range(w):
                if S[y][x] == 1:
                    counts[g][x] += 1
                    if counts[g][x] > k:
                        imp = True
                        break
        if imp:
            continue

        cuts = 0
        cum = [counts[g][0] for g in range(m)]
        for x in range(1, w):
            cut = False
            for g in range(m):
                cum[g] += counts[g][x]
                if cum[g] > k:
                    cut = True
                    break
            if cut:
                cuts += 1
                cum = [counts[g][x] for g in range(m)]
        ret = min(ret, m - 1 + cuts)
        #print(b, groups, m, cuts, ret)
    print(ret)
    return

def main():
    h, w, k = map(int, input().split())
    s = []
    for i in range(h):
        tmp = str(input())
        s.append([int(j) for j in tmp])
    solve(h, w, k, s)

if __name__ == '__main__':
    main()
