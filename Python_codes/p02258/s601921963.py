import sys

n = int(input())
r0 = int(input())
r1 = int(input())
p = r1 - r0
r = min(r0,r1)
for i in map(int, sys.stdin.readlines()):
    if p < i - r:
        p = i - r
    if r > i:
        r = i

print(p)