import sys

input = sys.stdin.readline
d = {}
for _ in range(int(input())):
    i = int(input())
    if i in d:
        del d[i]
    else:
        d[i] = True
print(len(d))