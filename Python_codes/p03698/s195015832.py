import math
import collections
import fractions
import itertools

def solve():
    s = list(input())
    if len(s) == len(set(s)):
        print("yes")
    else:
        print("no")
    return 0

if __name__ == "__main__":
    solve()