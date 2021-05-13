import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s, w = map(int, read().split())

print('unsafe' if w >= s else 'safe')