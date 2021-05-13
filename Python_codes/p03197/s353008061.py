import sys

read = sys.stdin.read

N, *a = map(int, read().split())
a = [i % 2 for i in a]
if 1 in a:
    print('first')
else:
    print('second')
