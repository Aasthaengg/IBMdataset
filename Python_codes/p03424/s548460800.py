import sys
import math
import bisect

def solve(A):
    if len(set(A)) == 3:
        return 'Three'
    else:
        return 'Four'

def main():
    n = int(input())
    A = input().split()
    print(solve(A))

if __name__ == "__main__":
    main()
