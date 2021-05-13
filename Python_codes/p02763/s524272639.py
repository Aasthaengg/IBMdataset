from collections import defaultdict
from bisect import bisect_left, insort_left
import sys
input = sys.stdin.readline
N = int(input())
S = list(input())

dic = defaultdict(list)
for i, s in enumerate(S):
    dic[s].append(i)

Q = int(input())
for _ in [0]*Q:
    t, *q = input().split()
    if t == '1':
        i, c = q
        i = int(i)-1

        s = S[i]
        if s == c:
            continue
        S[i] = c
        dic[s].pop(bisect_left(dic[s], i))
        insort_left(dic[c], i)

    else:
        l, r = map(int, q)
        l -= 1
        r -= 1
        cnt = 0
        for L in dic.values():
            i = bisect_left(L, l)
            if i != len(L) and L[i] <= r:
                cnt += 1
        print(cnt)
