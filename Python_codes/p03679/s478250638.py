import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x, a, b = map(int, readline().split())
if b - a <= 0:
    print('delicious')
elif (b - a) <= x:
    print('safe')
else:
    print('dangerous')