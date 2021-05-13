#!/usr/bin python3
# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ret = 0
    for a in range(N-2):
        for b in range(a+1,N-1):
#            a<b+c => a-b<c
#            b<c+a => b-a<c
#            c<a+b
# b-a<c<a+b
            rr = bisect_right(L[b+1:], L[a]+L[b]-1)
            ll = 0
            ret += rr - ll

    print(ret)

if __name__ == '__main__':
    main()
