import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    w = input()
    c = collections.Counter(w)
    for i in c:
        if c[i] % 2 == 1:
            print("No")
            exit()
    print("Yes")
    return 0

if __name__ == "__main__":
    solve()
