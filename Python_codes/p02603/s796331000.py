import math
import collections
import fractions
import itertools
import functools
import operator

def divis(l):
    seq = []
    beg, end = 0, 0
    le = len(l)
    for i in range(1,le):
        end = i
        if l[i] < l[i-1]:
            seq.append(l[beg:end])
            beg = i
    seq.append(l[beg:end+1])
    return seq

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = divis(a)
    yosan = 1000
    for i in a:
        yosan += (i[-1]-i[0])*(yosan//i[0])
    print(yosan)
    return 0

if __name__ == "__main__":
    solve()