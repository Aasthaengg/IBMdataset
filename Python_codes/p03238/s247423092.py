import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
if n == 1:
    print('Hello World')
else:
    print(sum(list(map(int, read().split()))))
