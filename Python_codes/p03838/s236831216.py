import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x, y = map(int, read().split())

def f(x, y):
    # + のみ
    if x <= y:
        yield y - x
    # 反転、+
    if -x <= y:
        yield 1 + x + y
    # +、反転
    if x <= -y:
        yield 1 - x - y
    # 反転、+、反転
    if -x <= -y:
        yield 2 - y + x

x = min(f(x, y))
print(x)