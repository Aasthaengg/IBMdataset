import sys
import numpy as np


def main():
    k = int(input())
    n = 50
    an = [n - 1 + (k // n) - (k % n) for _ in range(n)]
    for i in range(k % n):
        an[i] += n + 1
    print(n)
    print(*an)


main()
