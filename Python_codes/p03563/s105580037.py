import sys

a = []
for line in sys.stdin:
    a.append(int(line))
print(a[1] * 2 - a[0])