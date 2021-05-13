#!/usr/bin python3
# -*- coding: utf-8 -*-

def cnt(A, x):
    N = len(A)
    i = 0
    ret = 0
    while i<N:
        if A[i]<x:
            i += 1
        else:
            ret += 1
            while i<N and A[i]>=x:
                i += 1
    return ret

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ret = 0
    for i in range(1,101):
        ret += cnt(A,i)

    print(ret)

if __name__ == '__main__':
    main()