import sys
 
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()
nas = lambda: stdin.readline().split()

x, a = na()

if x < a:
    print(0)
else:
    print(10)