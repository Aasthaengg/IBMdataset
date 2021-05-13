#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    S = [0] * N
    P = [0] * N
    R = [0] * N
    for i in range(N):
        S[i] , P[i] = map(str, input().split())
    for i in range(N):
        R[i] = i + 1
    for i in range(N):
        P[i] = int(P[i]) * -1


    Z = zip(S, P, R)
    Z = sorted(Z)
    S, P, R = zip(*Z)

    for i in R:
        print(i)

if __name__ == '__main__':
    main()
