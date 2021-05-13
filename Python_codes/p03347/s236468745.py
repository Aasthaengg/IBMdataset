#!python
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    X = [0 for i in range(N)]
    A += [0]
    X += [0]

    count = 0

    if A[0] != 0:
        print(-1)
        return

    for i in range(N - 1, -1, -1):
        if A[i - 1] + 1 < A[i]:
            print(-1)
            return

        X[i] = max(0, X[i + 1] - 1)
        if A[i] == X[i]:
            continue

        count += A[i]
        X[i] = A[i]

    print(count)


if __name__ == '__main__':
    main()
