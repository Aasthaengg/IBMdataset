import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c, k = map(int, read().split())
print((a+b+c)-max(a, b, c)+max(a, b, c)*2**k)
