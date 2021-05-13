import sys
import numpy as np


def main():
    n = int(input())
    a = np.array([int(x) for x in input().split()])
    a -= np.arange(1, n + 1)
    a -= int(np.median(a))
    print(np.sum(np.abs(a)))


main()
