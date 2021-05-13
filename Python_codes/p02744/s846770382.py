import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

def solve():
    n = int(input())
    sushi = ["a"]
    alt = [chr(ord("a") + i) for i in range(n)]
    for i in range(n-1):
        sushi = [ans + x for ans in sushi for x in alt[:len(set(ans)) + 1]]
    for i in sushi:
        print(i)
    return 0

if __name__ == "__main__":
    solve()