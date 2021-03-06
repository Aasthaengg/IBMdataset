#!/usr/bin/env python3
# cython: profile=True
import sys

YES = "POSSIBLE"  # type: str
NO = "IMPOSSIBLE"  # type: str


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    AB = sorted(zip(a, b))
    s = set([b for a, b in AB if a == 1])
    g = set([a for a, b in AB if b == N])
    return YES if s & g else NO

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    print(solve(N, M, a, b))

def test():
    import doctest
    doctest.testmod()

def perf():
    import cProfile
    cProfile.run("main()")

if __name__ == '__main__':
    #test()
    #perf()
    main()
