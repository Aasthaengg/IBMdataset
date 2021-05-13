import sys
import math
import numpy as np
import copy

def main():
    a, b, c = map(int, input().split())
    x = sorted([a, b, c])
    print(10*x[2]+x[1]+x[0])

    return 0

if __name__ == '__main__':
    sys.exit(main())