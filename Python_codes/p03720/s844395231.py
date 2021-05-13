import sys
import math
import bisect

def main():
    n, m = map(int, input().split())
    A = [0] * n
    for i in range(m):
        a, b = map(int, input().split())
        A[a-1] += 1
        A[b-1] += 1
    for a in A:
        print(a)

if __name__ == "__main__":
    main()
