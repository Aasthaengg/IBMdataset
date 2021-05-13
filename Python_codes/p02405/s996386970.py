import sys

d = sys.stdin.readlines()
for i in d:
    h, w = [int(x) for x in i.split()]
    if h == w == 0:
        break
    for j in range(h):
        print(('#.' * w)[j % 2:][:w])
    print()