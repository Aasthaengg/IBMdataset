import sys
from copy import copy
input = sys.stdin.readline
'''
n, m = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))
S = input().strip()
for test in range(int(input())):
'''
inf = 100000000000000000  # 1e17
mod = 998244353


def two(x):
    return "0" * (h - 1 - len(bin(x)[2:])) + bin(x)[2:]


h, w, k = map(int, input().split())
S = []
ans = inf
for i in range(h):
    S.append(input().strip())
for way_cut in range(1 << (h - 1)):
    way_cut = two(way_cut)
    number_cut_horizontal = way_cut.count("1")
    number_cut_vertical = 0
    CUT = [-1]
    for i in range(len(way_cut)):
        if way_cut[i] == '1':
            CUT.append(i)
    CUT.append(len(way_cut))
    SUM = [0] * (w)
    PRE = [0] * (w)
    for col in range(w):
        for i in range(1, len(CUT)):
            for between in range(CUT[i - 1] + 1, CUT[i] + 1):
                SUM[i] += 1 if S[between][col] == "1" else 0
        isok = True
        for i in range(1, len(CUT)):
            if PRE[i] + SUM[i] > k:
                isok = False
        if not isok:
            number_cut_vertical += 1
            PRE = copy(SUM)
            SUM = [0]*(w)  # leave out
            # recheck
            for i in range(1, len(CUT)):
                if PRE[i] > k:
                    number_cut_vertical = inf
                    break
        else:
            for i in range(1, len(CUT)):
                PRE[i] += SUM[i]
                SUM[i] = 0
    ans = min(ans, number_cut_vertical + number_cut_horizontal)
print(ans)
