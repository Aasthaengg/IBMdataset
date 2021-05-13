import sys
 
stdin = sys.stdin

mod = 1000000007
inf = 1 << 60
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()
nas = lambda: stdin.readline().split()

a, b = na()

if a > 8 or b > 8:
    print(":(")
else:
    print("Yay!")