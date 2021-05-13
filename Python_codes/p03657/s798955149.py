import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b = map(int, readline().split())
if a % 3 == 0 or b % 3 == 0 or(a + b) % 3 == 0:
    print('Possible')
else:
    print('Impossible')