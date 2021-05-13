import sys
import math
import bisect

def solve(a, b):
    n = b - a - 1
    A = sum(list(range(1, n + 1)))
    return A - a

def main():
    a, b = map(int, input().split())
    print(solve(a, b))

if __name__ == "__main__":
    main()
