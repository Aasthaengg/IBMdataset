#!/usr/bin/env python3

def main():
    A, B, C, K = map(int, open(0).read().split())

    if abs(A - B) > 10**18:
        print('Unfair')
    else:
        if K % 2:
            print(B - A)
        else:
            print(A - B)


main()