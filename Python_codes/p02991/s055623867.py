import sys,os,math
from collections import Counter, defaultdict, deque
import bisect
from sys import stdin, stdout
from itertools import repeat
import Queue



# n, k = map(int, raw_input().split())
# da = map(int, raw_input().split())
# db = map(int, raw_input().split())


def main():
    n, m = map(int, raw_input().split())
    G = [[] for i in range(n+1)]
    ss = set()
    for i in range(m):
        a, b = map(int, raw_input().split())
        G[a].append(b)
    s, t = map(int, raw_input().split())
    t = t<<2
    q = deque()
    q.append((s<<2, 0))
    ss.add(s<<2)
    while q:
        st, step = q.popleft()
        point, mod = st>>2, st&3
        # print point, step, mod
        if st == t:
            print step/3
            return

        for adj in G[point]:
            new_st = (adj<<2) + (mod+1)%3
            if new_st not in ss:
                ss.add(new_st)
                q.append((new_st, step+1))
    print -1

main()
