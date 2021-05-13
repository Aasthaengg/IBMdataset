import sys
import math
import bisect


def main():
    r, d, x = map(int, input().split())
    A = []
    for _ in range(10):
        x = r * x - d
        A.append(x)
    for a in A:
        print(a)

if __name__ == "__main__":
    main()
