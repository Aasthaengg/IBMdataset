import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

h, w = inintm()
C = []

for _ in range(h):
    C.append(input())

for c in C:
    print(c)
    print(c)
