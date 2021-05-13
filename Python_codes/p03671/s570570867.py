import sys
 
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda x: [na() for _ in range(x)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda x: [ns() for _ in range(x)]
nas = lambda: stdin.readline().split()

a = na()
a.sort()
print(a[0] + a[1])