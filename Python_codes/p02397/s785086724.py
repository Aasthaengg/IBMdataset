import sys

n = sys.stdin.readlines()
for i in n:
    a, b = [int(x) for x in i.split()]
    if a == 0 and b == 0:
        break
    if a < b:
        print(a, b)
    else:
        print(b, a)