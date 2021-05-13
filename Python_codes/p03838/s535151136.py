import sys

x, y = map(int, input().split())
cnt = 0
if abs(x) == abs(y):
    print(1)
elif abs(x) < abs(y):
    while x < 0:
        x *= -1
        cnt += 1
    while abs(x) != abs(y):
        cnt += abs(y) - abs(x)
        x += abs(y) - abs(x)
    if x == y:
        print(cnt)
    else:
        print(cnt+1)
else:
    while x > 0:
        x *= -1
        cnt += 1
    while abs(x) != abs(y):
        cnt += abs(x) - abs(y)
        x += abs(x) - abs(y)
    if x == y:
        print(cnt)
    else:
        print(cnt+1)