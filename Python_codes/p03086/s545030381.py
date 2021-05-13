import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    s = input()
    size = len(s)
    ans = 0
    for beg in range(size):
        for end in range(beg+1, size+1):
            if all('ACGT'.count(c) == 1 for c in s[beg:end]):
                ans = max(ans, end-beg)
    print(ans)
    return 0

if __name__ == "__main__":
    solve()
