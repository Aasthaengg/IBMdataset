import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = list(readline().decode().rstrip())
print('Yes' if '9' in n else 'No')