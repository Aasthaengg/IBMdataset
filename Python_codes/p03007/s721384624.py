#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    s = A[0]
    l = A[-1]
    ret = []
    for a in A[1:N-1]:
        if a>=0:
            ret.append((s, a))
            s -= a
        else:
            ret.append((l, a))
            l -= a
    print(l-s)
    ret.append((l,s))
    for x, y in ret:
        print(x, y)

if __name__ == '__main__':
    main()