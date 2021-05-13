import sys
import math
import bisect

def solve(n):
    return math.floor(math.sqrt(n)) ** 2

def main():
    n = int(input())
    print(solve(n))

if __name__ == "__main__":
    main()
