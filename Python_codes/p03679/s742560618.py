import sys

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

X, A, B = rl()
print('delicious' if A >= B else 'safe' if X >= B - A else 'dangerous')