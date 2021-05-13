#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    size = A[0]
    ret = 1
    for i in range(1, N):
        if A[i]<=2*size:
            size += A[i]
            ret += 1
        else:
            size += A[i]
            ret = 1
    print(ret)

if __name__ == '__main__':
    main()