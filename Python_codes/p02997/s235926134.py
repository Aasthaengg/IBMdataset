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
    n, k = map(int, raw_input().split())
    ans = []
    if k > (n-1)*(n-2)/2:
        print -1
        return
    for i in range(1, n):
        ans.append((n, i))
    k -= (n-1)*(n-2)/2
    for i in range(1, n):
        for j in range(i+1, n):
            if k>=0:
                continue
            k += 1
            ans.append((i, j))
    print len(ans)
    print '\n'.join(map(lambda a:"%s %s"% (a[0],a[-1]), ans))
        


main()
