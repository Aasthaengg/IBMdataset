import sys
 
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda x: [na() for _ in range(x)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda x: [ns() for _ in range(x)]
nas = lambda: stdin.readline().split()

a, b = na()

if b < a:
    print(a - 1)
else:
    print(a)