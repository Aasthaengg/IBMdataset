import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

N = int(input())

def solve():
    mod = 10**9+7
    ans = 10**N - (9**N)*2 + 8**N
    ans %= mod
    print(ans)
    return 0

if __name__ == "__main__":
    solve()
