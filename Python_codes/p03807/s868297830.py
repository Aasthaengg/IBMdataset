#!/usr/bin/env python3
import sys
# input = sys.stdin.r/eadline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    N = INT()
    A = LI()
    count = 0
    for i in range(N):
        if A[i]&1:
            count += 1
    if count&1:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()
