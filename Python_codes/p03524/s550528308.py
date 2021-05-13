import sys
input = sys.stdin.readline
from collections import Counter


def read():
    S = input().strip()
    return S,


def solve(S):
    C = Counter(S) + Counter("abc")
    V = list(sorted(C.values()))
    if V[-1] - V[0] <= 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
