import os, sys, re, math

A,B = list(map(int,input().split(' ')))

if B % A == 0:
    print(str(B+A))
else:
    print(str(B-A))
