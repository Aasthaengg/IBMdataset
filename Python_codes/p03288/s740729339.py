import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

r = ni()
if r < 1200:
    print("ABC")
elif 1200 <= r < 2800:
    print("ARC")
else:
    print('AGC')
