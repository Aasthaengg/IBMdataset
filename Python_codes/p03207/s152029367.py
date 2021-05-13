import sys
import math
import bisect

def main():
    n = int(input())
    A = []
    for i in range(n):
        A.append(int(input()))
    A.sort()
    A[-1] //= 2
    print(sum(A))

if __name__ == "__main__":
    main()
