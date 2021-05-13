import sys,os,math
from collections import Counter, defaultdict, deque
import bisect
from sys import stdin, stdout
from itertools import repeat
import Queue


# sys.stdin = open('input')
# n, k = map(int, raw_input().split())
# da = map(int, raw_input().split())
# db = map(int, raw_input().split())


def main():
    n = map(int, raw_input().split())[0]
    da = [map(int, raw_input().split()) for i in range(n)]
    need = [0 for i in range(n+2)]
    t = [0 for i in range(n+2)]
    idx = [0 for i in range(n+2)]
    l = n*(n-1)/2
    ans = 0
    q = deque()
    for i in range(1, n+1):
        da[i-1].append(n+1)
        need[i] = da[i-1][idx[i]]
        if i == need[need[i]]:
            q.append(i);
    # print da
    while q:
        # print q
        fr = q.popleft()
        x, y = fr, need[fr]
        # print x,y,"sssssssss"
        # print need
        if not (x == need[y] and y == need[x]):
            continue
        ti = max(t[x], t[y]) + 1
        t[x] = t[y] = ti
        ans = max(ans, ti)
        l-=1
        idx[x] += 1
        idx[y] += 1
        need[x] = da[x-1][idx[x]]
        need[y] = da[y-1][idx[y]]
        if x == need[need[x]]:
            q.append(x)
        if y == need[need[y]]:
            q.append(y)
    # print l
    if l==0:
        print ans
    else:
        print -1






main()
