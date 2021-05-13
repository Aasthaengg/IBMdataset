import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

r = int(readline())
if r < 1200:
    print('ABC')
elif r < 2800:
    print('ARC')
else:
    print('AGC')
