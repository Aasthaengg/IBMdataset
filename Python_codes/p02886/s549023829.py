#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    d = list(map(int, input().split()))
    ret = 0
    for i in range(N):
        for j in range(i+1,N):
            ret += d[i]*d[j]
    print(ret)

if __name__ == '__main__':
    main()