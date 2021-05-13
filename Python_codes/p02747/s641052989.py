import sys
import math
import bisect

def solve(s):
    n = len(s)
    if n % 2 == 1:
        return False
    for i in range(0, n, 2):
        if s[i:i+2] != 'hi':
            return False
    return True

def main():
    if solve(input()):
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
