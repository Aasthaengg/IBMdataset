#!/usr/bin/env python3
import sys
from itertools import chain

def solve(X: int, N: int, p: "List[int]"):
    p = set(p)
    for d in range(0, 100):
        x = X - d
        if x not in p:
            return x
        x = X + d
        if x not in p:
            return x

def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # X, N, p = map(int, line.split())
    X = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(X, N, p)
    print(answer)

if __name__ == '__main__':
    main()
