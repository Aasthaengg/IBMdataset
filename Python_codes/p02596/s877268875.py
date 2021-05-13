#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(K: int):
    cur = 0
    for i in range(K):
        cur += pow(10, i, K) * 7
        cur %= K
        if cur == 0:
            print(i + 1)
            return i + 1
    ret = -1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)

if __name__ == '__main__':
    main()
