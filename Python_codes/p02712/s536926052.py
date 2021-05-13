import sys
import numpy as np


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = np.arange(n+1, dtype=int)
    a[3:n+1:3] = 0
    a[5:n+1:5] = 0
    print(np.sum(a))


if __name__ == '__main__':
    main()
