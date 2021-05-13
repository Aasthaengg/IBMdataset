import sys
input = sys.stdin.readline


def read():
    S = input().strip()
    return S,


def solve(S):
    u = set(S)
    return "yes" if len(u) == len(S) else "no"


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
