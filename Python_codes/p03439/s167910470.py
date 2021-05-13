#!/usr/bin python3
# -*- coding: utf-8 -*-

import sys

def main():
    N = int(input())
    L = 0
    print(L)
    sys.stdout.flush()
    Ls = input()
    if Ls == "Vacant":
        exit()
    U = N-1
    print(U)
    sys.stdout.flush()
    Us = input()
    if Us == "Vacant":
        exit()
    for _ in range(18):
        mid = (U+L)//2
        if mid%2==1:
            mid-=1
        if mid==L:
            mid+=1
        print(mid)
        sys.stdout.flush()
        ms = input()
        if ms == "Vacant":
            exit()
        if Ls==ms:
            L=mid
        if Us==ms:
            U=mid

if __name__ == '__main__':
    main()