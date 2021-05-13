import sys
import math
import numpy as np
import copy

def main():
    n, m, nx, ny = map(int, input().split())
    x = [int(t) for t in input().split()]
    y = [int(t) for t in input().split()]
    x.sort()
    y.sort()
    if x[-1] < y[0] and y[0] > nx and x[-1] < ny:
        print("No War")
    else:
        print("War")

    return 0

if __name__ == '__main__':
    sys.exit(main())