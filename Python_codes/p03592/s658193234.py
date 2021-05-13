import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n,m,k = na()

for i in range(m+1):
    for j in range(n+1):
        if n*i+m*j-2*i*j == k:
            print('Yes')
            exit()

print('No')