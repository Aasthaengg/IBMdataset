#!/usr/bin python3
# -*- coding: utf-8 -*-

def od(n):
    ret = set([])
    for i in range(n):
        for j in range(i+1,n):
            if i+j+2 != n+1:
                ret.add((i+1, j+1))
    return ret

def main():
    N = int(input())

    ret = od(N//2*2)
    if N%2==1:
        for i in range(N-1):
            ret.add((i+1, N))

    print(len(ret))
    for x, y in ret:
        print(x,y)



if __name__ == '__main__':
    main()