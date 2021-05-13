import sys

read = sys.stdin.read

N, *a = map(int, read().split())
a = [i for i in a if i % 2 == 1]
if len(a) > 0:
    print('first')
else:
    print('second')
