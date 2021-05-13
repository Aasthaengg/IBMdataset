#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ret = 0
    for i in range(1,N):
        if A[i]==A[i-1]:
            ret+=1
            A[i]=1000

    print(ret)

if __name__ == '__main__':
    main()