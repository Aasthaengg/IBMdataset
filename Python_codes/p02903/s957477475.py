import sys
 
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()
nas = lambda: stdin.readline().split()

h, w, a, b = na()
d1 = [1, 0]
d2 = [0, 1]

c = d1
for i in range(h):
    if i == b:
        c = d2
    for j in range(w):
        if j >= a:
            print(c[1], end='')
        else:
            print(c[0], end='')
    print()