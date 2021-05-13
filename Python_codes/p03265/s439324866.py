import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

x1, y1, x2, y2 = inintm()

print("{} {} {} {}".format(x2-(y2-y1), y2+(x2-x1), x1-(y2-y1), y1+(x2-x1)))