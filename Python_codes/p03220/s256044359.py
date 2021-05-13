#!/usr/bin/env python3


def main():
    import numpy as np

    N, T, A, *H = map(int, open(0).read().split())
    print(np.argmin(np.abs(A - (T - np.array(H) * 0.006))) + 1)


main()
