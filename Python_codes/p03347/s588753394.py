#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    nw = -1
    ret = 0
    for i, a in enumerate(A):
        if i<a or nw+1<a:
            print(-1)
            exit()
        elif i == 0:
            nw = 0
            continue
        elif nw+1==a:
            nw += 1
            continue
        else:
            ret += nw
            nw = a
    ret += a
#            print(i,ret)
    print(ret)

if __name__ == '__main__':
    main()