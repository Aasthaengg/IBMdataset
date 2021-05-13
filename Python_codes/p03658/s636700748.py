import sys
import math
import bisect

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[-m:]))

if __name__ == "__main__":
    main()
