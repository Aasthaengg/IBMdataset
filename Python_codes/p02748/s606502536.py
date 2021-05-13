import sys

A, B, M = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
xyc = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(M)]
ans = min(a) + min(b)

for xyci in xyc:
    x, y, c = xyci
    tmp = a[x - 1] + b[y - 1] - c
    if ans > tmp:
        ans = tmp

print(ans)