import sys

N, X = map(int, input().split())
L = list(map(int, sys.stdin.readline().rsplit()))

d = 0
res = 1
for l in L:
    if d + l > X:
        break
    d += l
    res += 1

print(res)
