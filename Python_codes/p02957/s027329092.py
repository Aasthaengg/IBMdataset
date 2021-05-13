#!/usr/bin/env python3

def main():
    A, B = map(int, open(0).read().split())

    if (A - B) % 2 == 0:
        if A > B:
            print(A - int(abs(A - B) / 2))
        else:
            print(B - int(abs(A - B) / 2))
    else:
        print('IMPOSSIBLE')


main()