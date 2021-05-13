import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

H,W = map(int,input().split())
grid = '*' * (W+2)
for _ in range(H):
    grid += '*' + input().rstrip() + '*'
grid += '*' * (W+2)

move = [1,-1,W+2,-(W+2)]

root = [None if x == '*' else -1 for x in grid]

answer = 0
for i in range((H+2)*(W+2)):
    if root[i] != -1:
        continue
    q = [i]
    root[i] = i
    counter = defaultdict(int)
    while q:
        x = q.pop()
        counter[grid[x]] += 1 
        for dx in move:
            y = x + dx
            if root[y] != -1:
                continue
            if grid[x] == grid[y]:
                continue
            root[y] = i
            q.append(y)
    answer += counter['.'] * counter['#']

print(answer)