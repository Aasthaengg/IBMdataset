import sys

k = int(input())
a = list(map(int, input().split()))


x, y = 2, 2

for i in range(k-1, -1, -1):
    minx = x + (a[i] - x % a[i]) % a[i]
    maxx = y - y % a[i]
    if minx > maxx:
        print(-1)
        sys.exit(0)
    else:
        x, y = minx, maxx + a[i] - 1


print(x, y)
