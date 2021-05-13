import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c, d = map(int, readline().split())
if a + b > c + d:
    print('Left')
elif a + b < c + d:
    print('Right')
else:
    print('Balanced')
