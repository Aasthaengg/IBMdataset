#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    T = sorted((set(S)))
    l = len(T)

    D = {}
    for i in range(l):
        D[T[i]] = 0
    for i in range(N):
        D[S[i]] += 1

    m = max(D.values())
    for i in range(l):
        if D[T[i]] == m:
            print(T[i])


if __name__ == '__main__':
    main()
