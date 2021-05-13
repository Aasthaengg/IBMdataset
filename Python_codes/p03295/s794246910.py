#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N, M = map(int,input().split())
    ab = [None] * M
    for m in range(M):
        a, b = map(int,input().split())
        ab[m] = [a,b]
    ab.sort(key=lambda x:x[1])
    ret = 1
    TMP = ab[0][1]
    for x in ab[1:]:
        if TMP<=x[0]:
            TMP = x[1]
            ret += 1
    print(ret)

if __name__ == '__main__':
    main()