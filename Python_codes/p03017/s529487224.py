#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N, A, B, C, D = map(int, input().split())
    S = input()

    ret = 'No'
    if C<D:
        pathBtoD=S[B-1:D]
        pathAtoC=S[A-1:C]
        if pathBtoD.find('##')==-1 and pathAtoC.find('##')==-1:
            ret = 'Yes'
    else:
        pathBtoD=S[B-1:D]
        pathAtoC=S[A-1:C]
        pathBtoD2 = S[B-2:D+1]
        if pathBtoD.find('##')==-1 and pathAtoC.find('##')==-1:
            if pathBtoD2.find('...')!=-1:
                ret = 'Yes'
    print(ret)

if __name__ == '__main__':
    main()