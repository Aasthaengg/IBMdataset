import sys
import math
import bisect

def solve(s):
    n = len(s)
    A = []
    for i in range(0, n, 2):
        A.append(s[i])
    return ''.join(A)

def main():
    print(solve(input()))

if __name__ == "__main__":
    main()
