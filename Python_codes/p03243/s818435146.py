import sys
import math
import bisect

def solve(n):
    while True:
        if len(set(list(str(n)))) == 1:
            return n
        n = n + 1

def main():
    n = int(input())
    print(solve(n))

if __name__ == "__main__":
    main()
