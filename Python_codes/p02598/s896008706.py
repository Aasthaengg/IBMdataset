from sys import stdin
input = stdin.buffer.readline
n, k = map(int, input().split())
*a, = map(int, input().split())
def f(mx):
    cnt = 0
    for i in a:
        cnt += (i + mx - 1) // mx - 1
    return cnt
l, r = 1, int(1e9)
while l < r:
    m = (l + r) >> 1
    if f(m) > k:
        l = m + 1
    else:
        r = m
print(r)
