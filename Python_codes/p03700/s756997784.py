from math import ceil

n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]


def f(x):
    cnt = 0
    for e in h:
        cnt += max(0, ceil((e - b * x) / (a - b)))

    if cnt > x:
        return False

    return True


l = 0
r = ceil(max(h) / b)
while r - l > 1:
    mid = (l + r) // 2
    if f(mid):
        r = mid
    else:
        l = mid

print(r)
