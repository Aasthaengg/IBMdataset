#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    S = [list(map(int,input().split())) for i in range(N)]
    ret = 0
    for i in range(N-1,-1,-1):
        A, B = S[i]
        x = (A+ret)%B
        if x!=0:
            ret += B - (A+ret)%B
    print(ret)

if __name__ == '__main__':
    main()