from sys import stdin
import sys
import numpy as np
import collections
from functools import cmp_to_key

##  input functions for me
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def rip(sep = ''):
    if sep == '' :
        return map(int, input().split()) 
    else: return map(int, input().split(sep))
def ria(sep = ''): 
    return list(rip(sep))
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##
def main():
    H, W, A, B = rip()
    a = [['0'] * W for i in range(H)]
    for i in range(B):
        for j in range(A):
            a[i][j] = '1'
    for i in range(B,H):
        for j in range(A,W):
            a[i][j] = '1'
    for i in range(H):
        print(''.join(a[i]))


if __name__ == "__main__":
    main()
