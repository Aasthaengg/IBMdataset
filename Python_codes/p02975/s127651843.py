#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Al = Counter(A)
    x = list(Al)
    x.sort()

    if len(Al)>3:
        print('No')
    elif len(Al)==3:
        cond1 = (x[0]^x[1]^x[2] == 0)
        cond2 = (Al[x[0]] == N//3) and (Al[x[1]] == N//3) and (Al[x[2]] == N//3)
        if cond1 and cond2:
            print('Yes')
        else:
            print('No')

    elif len(Al)==2:
        cond1 = x[0] == 0
        cond2 = (Al[x[0]] == N//3) and (Al[x[1]] == N - N//3)
        if cond1 and cond2:
            print('Yes')
        else:
            print('No')
    elif len(Al)==1:
        cond1 = x[0] == 0
        cond2 = True
        if cond1 and cond2:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()