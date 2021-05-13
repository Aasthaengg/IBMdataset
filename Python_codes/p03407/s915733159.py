import sys

stdin = sys.stdin
 
ni = lambda:int(ns())
na = lambda:list(map(int,stdin.readline().split()))
ns = lambda:stdin.readline().rstrip()  # ignore trailing spaces

A, B, C = na()
print('Yes' if A + B >= C else 'No')