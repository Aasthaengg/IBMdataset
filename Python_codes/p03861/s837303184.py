import sys,math,collections,itertools
input = sys.stdin.readline

A,B,X=list(map(int,input().split()))
print(B//X - (A-1)//X)
