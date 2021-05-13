import sys
import math
import bisect

def solve(a, b):
    if a % 3 == 0:
        return True
    if b % 3 == 0:
        return True
    if (a + b) % 3 == 0:
        return True
    return False

def main():
    a, b = map(int, input().split())
    if solve(a, b):
        print('Possible')
    else:
        print('Impossible')

if __name__ == "__main__":
    main()
