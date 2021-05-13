import sys
 
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda x: [na() for _ in range(x)]
ns = lambda: stdin.readline().rstrip()
nas = lambda: stdin.readline().split()

t, x = na()
print(t / x)