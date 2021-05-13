import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))

pre = 0
res = 0
for a in A:
    if a == pre:
        res += 1
        pre = 0
    else:
        pre = a

print(res)
