import sys

x, y = map(int, sys.stdin.readline().rstrip().split())
count = 0
if abs(x) < abs(y):
    if x < 0:
        count += 1
        x = -x
    if y < 0:
        count += 1
        y = -y
    count += abs(y - x)
    print(count)
else:
    if x > 0:
        count += 1
        x = -x
    if y > 0:
        count += 1
        y = -y
    count += abs(y - x)
    print(count)