import sys
import math
import bisect

def solve(n, m):
    for i in range(m + 1):
        if i > n:
            break
        if (n - i) % 500 == 0:
            return True
    return False

def main():
    n = int(input())
    m = int(input())
    if solve(n, m):
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
