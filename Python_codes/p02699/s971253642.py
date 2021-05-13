#! /usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)


INF=10**20
def solve(S: int, W: int):
    print("unsafe" if W >= S else "safe" )
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    solve(S, W)



if __name__ == "__main__":
    main()
