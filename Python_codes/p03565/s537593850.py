import sys
input = sys.stdin.readline


def read():
    S = list(input().strip())
    T = list(input().strip())
    return S, T


def solve(S, T):
    k = -1
    for i in range(len(S) - len(T), -1, -1):
        count = 0
        for j in range(len(T)):
            if S[i+j] in [T[j], "?"]:
                count += 1
        if count == len(T):
            k = i
            break
    if k == -1:
        return "UNRESTORABLE"
    for i in range(len(T)):
        S[k+i] = T[i]
    for i in range(len(S)):
        if S[i] == "?":
            S[i] = "a"
    return "".join(S)


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
