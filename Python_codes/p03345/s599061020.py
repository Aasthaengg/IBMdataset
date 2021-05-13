import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A,B,C,K = map(int,read().split())

x = A - B
if K&1:
    x *= (-1)
print(x)