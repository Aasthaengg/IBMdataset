#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    S = [None]*N
    for _ in range(N):
        a,b = map(int,input().split())
        S[_] = [a+b, a, b]
    S.sort(reverse = True)
    ret = 0
    for i in range(N):
        if i%2==0:
            ret += S[i][1]
        else:
            ret -= S[i][2]
#        print(i,ret)
    print(ret)

if __name__ == '__main__':
    main()