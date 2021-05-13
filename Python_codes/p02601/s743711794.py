import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    a, b, c = map(int, input().split())
    k = int(input())
    i = k+1
    for p in range(i):
        for q in range(i-p):
            for r in range(i-p-q):
                aa, bb, cc = a, b, c
                for k in range(p):
                    aa*=2
                for k in range(q):
                    bb*=2
                for k in range(r):
                    cc*=2
                if aa < bb < cc:
                    print("Yes")
                    exit()
    print("No")
    return 0

if __name__ == "__main__":
    solve()
