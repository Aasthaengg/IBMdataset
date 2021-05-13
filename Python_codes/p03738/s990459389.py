import sys

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # applies to numbers only
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

A = ri()
B = ri()
print('GREATER' if A > B else 'LESS' if A < B else 'EQUAL')