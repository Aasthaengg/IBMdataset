import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

h, w = inintm()

pixel = []
f = ""
l = ""

for i in range(w+2):
    f += "#"

pixel.append(f)

for i in range(h):
    pixel.append("#" + input() + "#")

for i in range(w+2):
    l += "#"

pixel.append(l)

for x in pixel:
    print(x)
