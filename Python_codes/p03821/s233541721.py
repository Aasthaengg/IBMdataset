import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()

bt = []
ans = 0

for i in range(n):
    a, b = inintm()
    bt.append([a, b])

for i in range(n)[::-1]:
    if (bt[i][0]+ans) % bt[i][1] != 0:
        ans += bt[i][1] - ((bt[i][0]+ans) % bt[i][1])

print(ans)