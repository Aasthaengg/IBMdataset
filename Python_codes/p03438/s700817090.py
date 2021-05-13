import sys
 
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
 
ni = lambda: int(ns())
nin = lambda y: [ni() for _ in range(y)]
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda y: [na() for _ in range(y)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda y: [ns() for _ in range(y)]
ncl = lambda y: [list(ns()) for _ in range(y)]
nas = lambda: stdin.readline().split()

n = ni()
a = na()
b = na()

p = 0
q = 0

for i in range(n):
    if a[i] < b[i]:
        m = b[i] - a[i]
        if m % 2 == 1:
            m -= 1
        p += m
    else:
        q += a[i] - b[i]

p //= 2

if p >= q:
    print("Yes")
else:
    print("No")