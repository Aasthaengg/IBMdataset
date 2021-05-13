import sys
sys.setrecursionlimit(10**6)

h,w = map(int,input().split())

sl = []

for _ in range(h):
    s = list(input())
    sl.append(s)

used = [-1 for i in range(h*w)]
def dfs(i, j):
    used[i] = j
    if i % w + 1 < w:
        if sl[i//w][i%w] != sl[i//w][i%w+1]:
            if used[i+1] == -1:
                dfs(i + 1, j)
    if i % w - 1 >= 0:
        if sl[i//w][i%w] != sl[i//w][i%w-1]:
            if used[i-1] == -1:
                dfs(i - 1, j)
    if i // w + 1 < h:
        if sl[i // w][i % w] != sl[i // w+1][i % w]:
            if used[i+w] == -1:
                dfs(i + w, j)
    if i // w - 1 >= 0:
        if sl[i // w][i % w] != sl[i // w-1][i % w]:
            if used[i-w] == -1:
                dfs(i -w, j)

while True:
    if min(used) >= 0:
        break
    for i, j in enumerate(used):
        if j == -1:
            dfs(i, i)

from collections import defaultdict
dic = defaultdict(list)

for i, j in enumerate(used):
    dic[j].append(i)

ans = 0
for group in dic.values():
    a = 0
    b = 0
    for p in group:
        i = p // w
        j = p % w
        if sl[i][j] == "#":
            a += 1
        else:
            b += 1
    ans += a*b
print(ans)
