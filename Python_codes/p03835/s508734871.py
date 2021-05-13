#!/usr/bin/env python3


def main():
    K, S = map(int, open(0).read().split())
    # n = 0
    # for X in range(K + 1):
    #     for Y in range(S - X + 1):
    #         if (Y <= K) & (S - X - Y <= K):
    #             n += 1
    # print(n)
    print(
        len(
            [
                0
                for X in range(K + 1)
                for Y in range(S - X + 1)
                if (Y <= K) & (S - X - Y <= K)
            ]
        )
    )


main()
