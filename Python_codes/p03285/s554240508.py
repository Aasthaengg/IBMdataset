#!/usr/bin/env python3


def main():
    N = int(input())
    for f in range((N // 4) + 1):
        for s in range((N // 7) + 1):
            if 4 * f + 7 * s == N:
                print("Yes")
                exit(0)
    print("No")


main()
