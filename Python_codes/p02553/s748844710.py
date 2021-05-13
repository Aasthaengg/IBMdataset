import numpy as np
import sys

if __name__ == "__main__":
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines

    a, b, c, d = map(int, readline().split())
    print(max(a * c, b * d, a * d, b * c))
