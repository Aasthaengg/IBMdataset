import sys

import numpy as np

readline = sys.stdin.buffer.readline


def main():
    H, W = map(int, readline().split())
    N = int(readline())
    A = list(map(int, readline().split()))
    B = np.ones([H * W], dtype=np.int32)

    s = 0
    for i, a in enumerate(A):
        B[s:s + a] = i + 1
        s += a

    B = np.reshape(B, [H, W])
    for i in range(H):
        if i % 2 == 1:
            B[i, :] = B[i, :][::-1]
        print(*B[i, :])


main()
