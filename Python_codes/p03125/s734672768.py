# coding: utf-8
from sys import stdin
A,B = map(int,stdin.readline().rstrip().split())
print( A + B if B % A == 0 else B - A) 