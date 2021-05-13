import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a = inint()
b = inint()

if a > b:
    print("GREATER")
elif a == b:
    print("EQUAL")
else:
    print("LESS")