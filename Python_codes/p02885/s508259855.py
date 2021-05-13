#!/usr/bin/env python3

def main():
    A, B = map(int, open(0).read().split())
    if (A >= B * 2):
        print(A - 2 * B)
    else:
        print(0)


main()