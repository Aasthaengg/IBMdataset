#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(S: str, T: str):
    ret = T + S
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)

if __name__ == '__main__':
    main()
