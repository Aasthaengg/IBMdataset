# coding: utf-8

# https://atcoder.jp/contests/abc110


def main():
    S = input()
    T = input()
    N = len(S)

    memo1 = {}
    memo2 = {}
    for i in range(N):
        if S[i] not in memo1:
            memo1[S[i]] = T[i]
        else:
            if memo1[S[i]] != T[i]:
                return "No"
        if T[i] not in memo2:
            memo2[T[i]] = S[i]
        else:
            if memo2[T[i]] != S[i]:
                return "No"

    return "Yes"


print(main())
