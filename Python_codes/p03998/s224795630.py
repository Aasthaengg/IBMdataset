#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    A = input()
    B = input()
    C = input()

    w = 'a'
    while True:
        if w == 'a':
            if A == '':
                print('A')
                exit()
            w = A[0]
            A = A[1:]
        if w == 'b':
            if B == '':
                print('B')
                exit()
            w = B[0]
            B = B[1:]
        if w == 'c':
            if C == '':
                print('C')
                exit()
            w = C[0]
            C = C[1:]


if __name__ == '__main__':
    main()
