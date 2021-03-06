#create date: 2020-07-03 22:02

import sys
stdin = sys.stdin
from itertools import groupby, accumulate

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n, k = na()
    s = ns()
    a = list()
    if s[0] == "0":
        a.append(0)
    gr = groupby(s)
    for key, group in gr:
        a.append(len(list(group)))
    if s[-1] == "0":
        a.append(0)
    acum = list(accumulate(a))
    m = len(acum)
    l = 2*k + 1
    if m == 1:
        print(acum[0])
        quit()
    if l > m:
        print(acum[-1])
        quit()
    ans = acum[l-1]
    for i in range(0, m-l+1, 2):
        ans = max(ans, acum[i+l-1] - acum[i-1])
    print(ans)

if __name__ == "__main__":
    main()