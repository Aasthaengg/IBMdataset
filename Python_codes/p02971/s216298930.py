#create date: 2020-07-07 11:02

import sys
stdin = sys.stdin
from heapq import heapify, heappush, heappop

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    a = list()
    for _ in range(n):
        a.append(ni())
    b = sorted(a, reverse=True)
    amax = b[0]
    asec = b[1]
    for ai in a:
        if ai == amax:
            print(asec)
        else:
            print(amax)


if __name__ == "__main__":
    main()