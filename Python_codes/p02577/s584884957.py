from sys import stdin
from math import ceil
inp = lambda : stdin.readline().strip()

ans = 0
for i in inp():
    i = int(i)
    ans += i
if ans%9:
    print('No')
else:
    print('Yes')