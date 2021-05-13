import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, d, x, *a = map(int, read().split())

cnt = 0
for i in a:
    if i == 1:
        cnt += d
    elif d % i == 0:
        cnt += d//i
    else:
        cnt += d // i + 1
print(cnt+x)
