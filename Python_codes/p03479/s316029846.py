from math import log
x, y = map(int, input().split())
for i in range(64):
    x *= 2
    if x > y:
        print(i + 1)
        exit()