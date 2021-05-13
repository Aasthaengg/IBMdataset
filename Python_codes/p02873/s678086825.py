#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    S = input()
    n = len(S)+1
    left=[0]*n
    right=[0]*n
    for i,s in enumerate(S):
        if s=='<':
            left[i+1]=left[i]+1
    for i,s in enumerate(S[::-1]):
        if s=='>':
            right[n-i-2]=right[n-i-1]+1
    ret =0
    for i in range(n):
        ret+= max(left[i],right[i])
    print(ret)

if __name__ == '__main__':
    main()