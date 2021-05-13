import itertools
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, q = map(int, readline().split())
s = readline().decode().rstrip()

lis = [0]*n
for i in range(n - 1):
    if s[i] + s[i + 1] == 'AC':
        lis[i+1] = 1

a = list(itertools.accumulate(lis))

for _ in range(q):
    l, r = map(int, readline().split())
    print(a[r-1]-a[l-1])