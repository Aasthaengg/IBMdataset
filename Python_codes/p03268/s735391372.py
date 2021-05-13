#!/usr/bin/env python3
import sys

def solve_even(N: int, K: int):
    return pow((N - (K//2)) // K + 1, 3) + pow((N - K) // K + 1, 3)

def solve(N: int, K: int):
    return pow(N // K, 3) if K % 2 else solve_even(N, K)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    print(solve(N, K))

if __name__ == '__main__':
    main()
