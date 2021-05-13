#!/usr/bin/env python3


def main():
    N = int(input())
    print(
        min(
            [
                sum(list(map(int, str(i)))) + sum(list(map(int, str(N - i))))
                for i in range(1, N)
            ]
        )
    )


main()
