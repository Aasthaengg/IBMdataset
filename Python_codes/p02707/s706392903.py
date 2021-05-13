#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    A = list(map(int, input().split()))

    l = [0] * N
    for i in A:
        l[i - 1] += 1

    for i in l:
        print(i)

if __name__ == '__main__':
    main()
