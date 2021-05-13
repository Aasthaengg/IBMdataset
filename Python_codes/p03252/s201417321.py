import sys
input = sys.stdin.readline
from collections import defaultdict


def read():
    S = input().strip()
    T = input().strip()
    return S, T


def solve(S, T):
    N = len(S)
    u2t = dict()
    t2u = dict()
    for i in range(N):
        if S[i] not in u2t:
            u2t[S[i]] = T[i]
        elif u2t[S[i]] != T[i]:
            return "No"
        if T[i] not in t2u:
            t2u[T[i]] = S[i]
        elif t2u[T[i]] != S[i]:
            return "No"
    return "Yes"


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
