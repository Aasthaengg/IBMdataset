import sys
 
stdin = sys.stdin

mod = 1000000007
inf = 1 << 60
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()
nas = lambda: stdin.readline().split()

n = ni()

p = n - 1
ans = p * (p + 1) // 2
print(ans)