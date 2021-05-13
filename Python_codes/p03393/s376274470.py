#!/usr/bin/env python3
import sys

def main():
    S = input()
    T = 'abcdefghijklmnopqrstuvwxyz'
    if len(S) < 26:
        U = set(T) - set(S)
        print(S + sorted(U)[0])
    else:
        if S == T[::-1]:
            print(-1)
        else:
            count = 1
            for i in range(25):
                if S[25-i] > S[24-i]:
                    break
                else:
                    count += 1
            #print(S[26-count:])
            for s in sorted(S[26-count:]):
                if s > S[25-count]:
                    print(S[:25-count] + s)
                    exit()

if __name__ == '__main__':
    main()
