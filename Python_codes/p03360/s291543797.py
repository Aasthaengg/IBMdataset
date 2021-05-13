import sys
import math
import bisect

def main():
    A = list(map(int, input().split()))
    A.sort()
    for _ in range(int(input())):
        A[-1] <<= 1
    print(sum(A))

if __name__ == "__main__":
    main()
