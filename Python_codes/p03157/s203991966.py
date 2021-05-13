import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
h, w = map(int, input().split())
n = h*w
fld = ''.join([input().rstrip()for _ in range(h)])


def to_v(i, j):
    return i*w+j


def generate_v2(v):
    i, j = divmod(v, w)
    if 0 < i:
        yield v-w
    if i < h-1:
        yield v+w
    if 0 < j:
        yield v-1
    if j < w-1:
        yield v+1


def dfs(v, c=0):
    if visited[v]:
        return
    visited[v] = 1
    cnt[c] += 1
    for v2 in generate_v2(v):
        if fld[v] == fld[v2]:
            continue
        dfs(v2, c ^ 1)


visited = [0]*n
ans = 0
for v in range(n):
    if visited[v]:
        continue
    cnt = [0, 0]
    dfs(v)
    ans += cnt[0]*cnt[1]
print(ans)