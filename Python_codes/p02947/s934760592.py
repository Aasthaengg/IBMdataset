import math
import collections
import fractions
import itertools
import functools
import  operator

def solve():
    n = int(input())
    s = ["".join(sorted(input())) for _ in range(n)]
    cnt = 0
    past = {}
    for i in range(n):
        si = s[i]
        if si in past:
            past[si] += 1
        else:
            past[si] = 1
    for i in past.values():
        cnt += i*(i-1)//2
    print(cnt)
    return 0

if __name__ == "__main__":
    solve()
