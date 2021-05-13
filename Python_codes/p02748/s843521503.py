from sys import stdin
from numpy import array
input = lambda: stdin.readline().rstrip()
na, nb, m = map(int, input().split())
a = array(list(map(int, input().split())))
b = array(list(map(int, input().split())))
ans = min(a) + min(b)
for i in range(m):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    ans = min(ans, a[x] + b[y] - c)
print(ans)