# https://atcoder.jp/contests/agc034/tasks/agc034_a
import sys
n, a, b, c, d = map(int, input().split())
s = list(input())

for i in range(a - 1, c - 1):
    if s[i] == '#' and s[i + 1] == '#':
        print('No')
        sys.exit()

for i in range(b - 1, d - 1):
    if s[i] == '#' and s[i + 1] == '#':
        print('No')
        sys.exit()

if c > d:
    f = False
    for i in range(b - 2, d - 1):
        if s[i] == '.' and s[i + 1] == '.' and s[i + 2] == '.':
            f = True
else:
    f = True
if f:
    print('Yes')
else:
    print('No')