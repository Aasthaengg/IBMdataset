#!/usr/bin/python3

import sys

def input():
    return sys.stdin.readline().rstrip('\n')

#S = input()
#A1,A2,A3 = list(map(int,input().split()))
A = int(input())
B = int(input())

C = [1,2,3]
C.remove(A)
C.remove(B)

print(C[0])
