import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s = input().strip()
a = set()
for i in s:
    if i in a:
        print('no')
        sys.exit()
    a.add(i)
print('yes')
