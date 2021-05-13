import sys

N, D = map(int, input().split())
cnt = 0
for s in sys.stdin.readlines():
    x, y = map(int, s.split())
    d = pow(x, 2) + pow(y, 2)
    cnt += (d <= pow(D, 2))
print(cnt)