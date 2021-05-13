import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, *x = map(int, read().split())

x2=sorted(x)
mid_left = x2[n // 2 - 1]
mid_right = x2[n // 2]

for v in x:
    if v <= mid_left:
        print(mid_right)
    else:
        print(mid_left)