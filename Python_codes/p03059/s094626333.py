import sys

def S(): return sys.stdin.readline().rstrip()

A,B,T = map(int,S().split())

print(T//A*B)