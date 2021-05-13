import sys
import math
import bisect

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[0:2]))

if __name__ == "__main__":
    main()
