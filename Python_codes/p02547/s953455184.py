import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

def solve():
    n = int(input())
    cnt = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a == b:
            cnt += 1
        else:
            cnt = 0
        if cnt > 2:
            print("Yes")
            exit()
    print("No")
    return 0

if __name__ == "__main__":
    solve()
