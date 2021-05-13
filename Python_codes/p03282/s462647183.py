#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    S = input()
    K = int(input())

    if K >= 1e3:
        K = 105

    T = ''
    for i in range(len(S)):
        if S[i] == '1':
            T += '1'
        else:
            T += S[i] * K

        if S[i] != '1':
            break

    print(T[K - 1])


if __name__ == '__main__':
    main()
