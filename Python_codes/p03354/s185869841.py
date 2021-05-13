import sys
from collections import deque
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# input処理を高速化する
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
p = list(map(int, input().split()))
p_inv = [0]*(N+1)
for i in range(1, N+1):
    p_inv[p[i-1]] = i

graph = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

stack = deque()
is_checked = [0] * (N+1)
links = [[] for _ in range(N+1)]
for i in range(1, N+1):
    stack.append(i)
    while stack:
        node = stack.pop()
        if is_checked[node]:
            continue

        links[i].append(node)
        for next in graph[node]:
            stack.append(next)

        is_checked[node] = 1

ans = 0
for l in links:
    check = set()
    for num in l:
        check.add(p_inv[num])
    l = set(l)
    ans += len(l & check)

print(ans)
