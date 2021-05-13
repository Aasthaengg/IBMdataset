#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ret = 1
    state = 0
    for i in range(1,N):
#        print(i,A[i],A[i-1],state,ret)
        if A[i]>A[i-1]:
            if state == -1:
                ret += 1
                state = 0
            else:
                state = 1
        elif A[i]<A[i-1]:
            if state == 1:
                ret += 1
                state = 0
            else:
                state = -1
#        print(i,A[i],A[i-1],state,ret)
    print(ret)

if __name__ == '__main__':
    main()