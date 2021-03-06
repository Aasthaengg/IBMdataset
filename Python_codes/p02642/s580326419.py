import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
from collections import Counter
def main():
    n, *a = map(int, read().split())

    if 1 in a:
        count1 = a.count(1)
        if count1 == 1:
            print(1)
            sys.exit()
        else:
            print(0)
            sys.exit()
    a = np.array(a)
    maxa = a.max()
    seq = np.zeros(maxa + 1, np.int32)
    u, cnt = np.unique(a, return_counts=True)
    for ue, cnte in zip(u, cnt):
        if cnte == 1:
            seq[ue] = 1
    for ae in a:
        t = ae * 2
        while t <= maxa:
            seq[t] = 0
            t += ae
    r = seq.sum()
    print(r)

if __name__ == '__main__':
    main()
