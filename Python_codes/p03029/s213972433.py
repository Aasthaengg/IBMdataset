#! /usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)


INF=10**20
def solve(A: int, P: int):
    ans = 3*A+P
    ans //= 2

    print(ans)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    solve(A, P)



if __name__ == "__main__":
    main()
