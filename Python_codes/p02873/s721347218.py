import sys

input = sys.stdin.readline


def left(N, S, a, i):
    a[i + 1] = 0
    v = 0
    while True:
        if i == 0:
            a[i] = v + 1
            break
        if S[i - 1] == ">":
            v += 1
            a[i] = v
            i -= 1
        else:
            a[i] = max(a[i], v + 1)
            break


def right(N, S, a, i):
    a[i] = 0
    v = 0
    while True:
        if i == N - 1:
            a[i + 1] = v + 1
            break
        if S[i + 1] == "<":
            i += 1
            v += 1
            a[i] = v
        else:
            a[i + 1] = max(a[i + 1], v + 1)
            break


def main():
    S = input().rstrip()
    N = len(S)

    a = [0] * (N + 1)
    if S[0] == "<":
        right(N, S, a, 0)
    if S[-1] == ">":
        left(N, S, a, N - 1)
    for i in range(N - 1):
        if S[i:i + 2] == "><":
            left(N, S, a, i)
            right(N, S, a, i + 1)
    
    ans = sum(a)
    print(ans)


if __name__ == "__main__":
    main()
