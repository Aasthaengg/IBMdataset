#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    S = input()

    T = S
    if len(S) == 3:
        T = ''
        for i in range(3):
            T += S[2 - i]
    print(T)

if __name__ == '__main__':
    main()
