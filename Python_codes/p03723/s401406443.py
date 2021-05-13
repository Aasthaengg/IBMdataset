#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**6)

def solve(a,b,c,counter=0):
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        return counter
    elif a == b == c: 
        return -1
    else:
        return solve((b+c)//2,(c+a)//2,(a+b)//2,counter+1)


def main():
    A, B, C = map(int,input().split())
    print(solve(A,B,C))

if __name__ == '__main__':
    main()
