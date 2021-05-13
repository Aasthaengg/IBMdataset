#!/usr/bin/env python3
import numpy as np


def solve(N, M, X, C, A):
    answer = float("inf")
    for ptn in range(1, 1 << len(C)):
        buy = [ptn & 1 << i == 1 << i for i in range(len(C))]
        if (A[buy].sum(axis=0).min() >= X) and (
            C[buy].sum() < answer
        ):
            answer = C[buy].sum()

    if answer == float("inf"):
        return -1

    return answer


def main():
    N, M, X = map(int, input().split())
    C = [None for _ in range(N)]
    A = [None for _ in range(N)]
    for i in range(N):
        C[i], *A[i] = map(int, input().split())
    C = np.array(C, dtype=np.uint32)
    A = np.array(A, dtype=np.uint32)
    answer = solve(N, M, X, C, A)
    print(answer)


if __name__ == "__main__":
    main()
