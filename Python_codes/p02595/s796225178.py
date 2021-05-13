#!/usr/bin/env python3
import sys
from itertools import chain


def solve(N: int, D: int, X: "List[int]", Y: "List[int]"):
    D2 = D * D
    answer = 0
    for x, y in zip(X, Y):
        if x * x + y * y <= D2:
            answer += 1
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N, D, X, Y = map(int, line.split())
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    answer = solve(N, D, X, Y)
    print(answer)


if __name__ == "__main__":
    main()
