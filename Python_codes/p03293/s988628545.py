import sys
input = sys.stdin.readline


def read():
    S = input().strip()
    T = input().strip()
    return S, T


def solve(S, T):
    N = len(S)
    for i in range(N):
        is_matched = True
        for j1 in range(N):
            j2 = (i + j1) % N
            if S[j1] != T[j2]:
                is_matched = False
                break
        if is_matched:
            return "Yes"
    return "No"


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
