#create date: 2020-07-03 18:05

import sys
stdin = sys.stdin
from collections import Counter

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    l = list()
    for i in range(n):
        s = ns()
        l.append("".join(sorted(s)))
    ans = 0
    for i in Counter(l).values():
        ans += (i * (i-1))//2
    print(ans)

if __name__ == "__main__":
    main()