import math
import collections
import fractions
import itertools
import functools
import  operator

def solve():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    c = collections.Counter(a)
    cnt = 0
    for i in c:
        if c[i] % 2 == 1:
            cnt += 1
    print(cnt)
    return 0

if __name__ == "__main__":
    solve()