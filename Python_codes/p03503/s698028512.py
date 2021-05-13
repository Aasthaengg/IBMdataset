import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools

n = int(readline())
f = [list(map(int, readline().split())) for _ in range(n)]
p = [list(map(int, readline().split())) for _ in range(n)]
bit = list(itertools.product([0, 1], repeat=10))
ans = -float('inf')
bit.pop(0)
for i in range(2 ** 10 - 1):
    memo = 0
    flag = False
    for j in range(n):
        cnt = 0
        for k in range(10):
            if bit[i][k] == f[j][k] == 1:
                cnt += 1
        if cnt != 0:
            flag = True
        memo += p[j][cnt]
    if flag:
        ans = max(ans, memo)
print(ans)
