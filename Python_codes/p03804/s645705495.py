#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    for w in range(N - M + 1):
        for h in range(N - M + 1):
            count = 0
            for i in range(M):
                if B[i] == A[i + h][w: w + M]:
                    count += 1
            if count == M:
                print('Yes')
                exit()
    print('No')


if __name__ == '__main__':
    main()
