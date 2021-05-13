import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c = map(int, readline().split())
if a == b:
    print(c)
elif b == c:
    print(a)
else:
    print(b)