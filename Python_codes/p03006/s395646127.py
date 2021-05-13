import copy
import math

N = int(input())
xy = []
for _ in range(N):
    xy.append(tuple(map(int, input().split())))

def dfs(parent, p, q):
    seen[parent] = True
    for child in range(N):
        # print(child)
        if seen[child] == False:
            x, y = xy[child]
            if x + p == xy[parent][0] and y + q == xy[parent][1] or \
                    x - p == xy[parent][0] and y - q == xy[parent][1]:
                dfs(child, p, q)


m = N
for i in range(N - 1):
    for j in range(i + 1, N):
        p = xy[i][0] - xy[j][0]
        q = xy[i][1] - xy[j][1]
        cnt = 0
        seen = [False] * N
        for start in range(N):
            if seen[start] == False:
                dfs(start, p, q)
                cnt += 1
                # print(tosee)
        m = min(cnt, m)
        # print(p, q, group)
print(m)