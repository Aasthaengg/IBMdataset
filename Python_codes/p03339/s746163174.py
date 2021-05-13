#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    E = [0] * (N+1)
    W = [0] * (N+1)
    for i, s in enumerate(S):
        E[i+1] = E[i] + (1 if s == 'W' else 0)
    for i, s in enumerate(reversed(S)):
        W[N-i-1] = W[N-i] + (1 if s == 'E' else 0)
    return min(e+w for e, w in zip(E, W))


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    print(solve(N, S))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()