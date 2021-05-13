import sys
input = sys.stdin.readline


def read():
    S = input().strip()
    return S,


def solve(S):
    if S[0] != "A":
        return "WA"
    c_index = -1
    for i in range(2, len(S)-1):
        if S[i] == "C":
            if c_index >= 0:
                return "WA"
            c_index = i
    if c_index == -1:
        return "WA"
    for i in range(1, len(S)):
        if i == c_index:
            continue
        elif S[i].lower() != S[i]:
            return "WA"
    return "AC"


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
