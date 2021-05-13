import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, m, x = inintm()
A = inintl()

h = 0
l = 0

for a in A:
    if a < x:
        l += 1
    else:
        h += 1

print(min(h, l))
