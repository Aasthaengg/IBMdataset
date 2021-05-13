import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s = sorted(read().decode().rstrip())
print('Yes' if ''.join(s) == 'abc' else 'No')
