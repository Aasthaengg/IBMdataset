import sys

d = sys.stdin.readlines()
for i in d:
    h, w = [int(x) for x in i.split()]
    if h == 0 and w == 0:
        break
    for i in range(h):
        print('#' * w)
    print('')