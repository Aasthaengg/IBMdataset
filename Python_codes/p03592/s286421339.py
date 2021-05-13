import sys
stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))

n, m, k = na()
for r in range(n+1):
    for c in range(m+1):
        s = n*m - r*c - (n-r)*(m-c)
        if k == s:
            print("Yes")
            quit()
print("No")