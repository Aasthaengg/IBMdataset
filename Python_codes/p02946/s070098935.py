import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

def solve():
    k, x = map(int, input().split())
    ans = []
    for i in range(max(-1000000, x-k+1), min(1000000, x+k)):
        ans.append(str(i))
    print(" ".join(ans))
    return 0

if __name__ == "__main__":
    solve()