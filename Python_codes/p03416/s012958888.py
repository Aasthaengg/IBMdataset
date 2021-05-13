#!/usr/bin/env python3


def main():
    A, B = map(int, open(0).read().split())
    print(
        len([0 for i in range(A, B + 1) if str(i) == "".join(list(reversed(str(i))))])
    )


main()
