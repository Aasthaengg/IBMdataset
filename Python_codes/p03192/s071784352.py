#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = input()
    print(N.count('2'))

if __name__ == '__main__':
    main()
