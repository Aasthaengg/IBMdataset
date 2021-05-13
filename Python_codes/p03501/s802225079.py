import sys

stdin = sys.stdin
 
ni = lambda:int(ns())
nl = lambda:list(map(int,stdin.readline().split()))
ns = lambda:stdin.readline().rstrip()  # ignore trailing spaces

N, A, B = nl()
print(min(N * A, B))