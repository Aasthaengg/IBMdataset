import math
import collections
import fractions
import itertools

def solve():
    a = int(input())
    b = int(input())
    if a > b:
        print("GREATER")
    elif a < b:
        print("LESS")
    else:
        print("EQUAL")
    return 0

if __name__ == '__main__':
    solve()