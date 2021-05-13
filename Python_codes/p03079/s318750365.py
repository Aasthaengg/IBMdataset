#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    A, B, C = map(int, input().split())
    if A == B == C:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
