import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())

for i in range(111, 1000, 111):
    if i >= n:
        print(i)
        exit()
