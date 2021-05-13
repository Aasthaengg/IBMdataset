from sys import stdin
import math
n,k = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
d = math.floor(math.log2(k))
next = [[-1 for _ in range(n)] for _ in range(d+1)]
for i in range(n):
    next[0][i] = a[i] - 1
for j in range(d):
    for i in range(n):
        if next[j][i] == -1:
            continue
        next[j+1][i] = next[j][next[j][i]]
cur = 0
i = 0
while k > 0:
    if k&1:
        cur = next[i][cur]
    k >>= 1
    i += 1
print(cur+1)
