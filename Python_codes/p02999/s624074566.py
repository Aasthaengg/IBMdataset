# Rounding
# https://atcoder.jp/contests/abc130/tasks/abc130_a

from sys import stdin, stdout

x, a = map(int, stdin.readline().split())
if x < a:
    stdout.write("0\n")
else:
    stdout.write("10\n")
