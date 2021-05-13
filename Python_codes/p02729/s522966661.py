# -*- coding: utf-8 -*-

def main():

    N, M = map(int, input().split())

    numN = N * (N - 1) / 2
    numM = M * (M - 1) / 2

    ans = 0

    if numN >= 0:
        ans += numN

    if numM >= 0:
        ans += numM

    print(int(ans))


if __name__ == "__main__":
    main()