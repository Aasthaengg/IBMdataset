import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())


w, h, x, y = inintm()

if x == w/2 and y == h/2:
    print("{} {}".format(w*h/2, 1))
else:
    print("{} {}".format(w*h/2, 0))