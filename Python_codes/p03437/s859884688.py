import sys
x, y = map(int, input().split())

if x % y == 0:
    print(-1)
    sys.exit(0)
i = 2
while(True):
    v = x * i
    if v > 10 ** 18:
        print(-1)
        sys.exit(0)
    if v % y != 0:
        print(v)
        sys.exit(0)
    i += 1