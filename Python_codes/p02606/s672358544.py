import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

L, R, D = map(int, read().split())

print(R//D - (L-1) // D)