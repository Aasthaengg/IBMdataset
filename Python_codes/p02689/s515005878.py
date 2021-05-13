#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    l = [1] * N
    for i in range(M):
        if H[A[i] - 1] < H[B[i] - 1]:
            l[A[i] - 1] -= 1
        elif H[A[i] - 1] > H[B[i] - 1]:
            l[B[i] - 1] -= 1
        else:
            l[A[i] - 1] -= 1
            l[B[i] - 1] -= 1
    print(l.count(1))

if __name__ == '__main__':
    main()
