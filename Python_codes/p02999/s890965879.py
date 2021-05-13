#!/usr/bin/env python3

def main():
    X, A = map(int, open(0).read().split())

    if (X < A):
        print(0)
    else:
        print(10)


main()