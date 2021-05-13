import sys

def S(): return sys.stdin.readline().rstrip()

A,B = map(int,S().split())

print(max(0,A-2*B))