import sys

input = sys.stdin.readline
t, x, y = 0, 0, 0
for _ in range(int(input())):
    t1, x1, y1 = map(int, input().split())
    a = abs(x1 - x) + abs(y1 - y)
    b = t1 - t
    if a <= b and a % 2 == b % 2:
        t, x, y = t1, x1, y1
    else:
        print("No")
        break
else:
    print("Yes")