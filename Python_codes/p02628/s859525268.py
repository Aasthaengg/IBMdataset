import numpy as np
import sys

if __name__ == "__main__":
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines

    n, k = map(int, readline().split())
    p = np.array(readline().split(), np.int64)

    p = np.sort(p)
    print(p[:k].sum())
