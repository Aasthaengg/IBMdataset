from sys import stdin
from math import ceil
inp = lambda : stdin.readline().strip()

n = int(inp())
a = [int(x) for x in inp().split()]

curr = 0
ans = 0
for i in a:
    curr = max(curr, i)
    if i < curr:
        ans += curr - i
print(ans)