# coding: utf-8
import sys
from bisect import bisect_left, bisect_right, insort_left
from collections import defaultdict

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 各アルファベットのindexのリストを作り,bisect_left()
N = ir()
S = list(sr())
dic = defaultdict(list)
for i, s in enumerate(S):
    dic[s].append(i)

Q = ir()
for _ in range(Q):
    a, b, c = sr().split()
    if a == '1':
        b = int(b) - 1
        if S[b] == c:
            continue
        dic[S[b]].remove(b)
        insort_left(dic[c], b)
        S[b] = c
    else:
        b = int(b) - 1; c = int(c) - 1
        kind = 0
        for x in range(26):
            word = chr(ord('a')+x)
            if len(dic[word]) == 0:
                continue
            i = bisect_left(dic[word], b)
            j = bisect_right(dic[word], c)
            if i != j:
                kind += 1
        print(kind)

# 07