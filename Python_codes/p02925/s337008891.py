from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n = int(input())
A = []
M = [[-1 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        M[i][j] = cnt
        M[j][i] = cnt
        cnt += 1
ans = 0
nodes = []
adjacent_list = [[] for i in range(n*(n-1)//2)]
for i in range(n):
    tmp = list(map(int, input().split()))
    pre = tmp[0] - 1
    for j in tmp[1:]:
        adjacent_list[M[i][pre]].append(M[i][j-1])
        pre = j - 1
#まず、閉路検
seen = defaultdict(lambda: False)
visited = defaultdict(lambda: False)
def check(node):
    if visited[node]:
        return
    seen[node] = True
    for i in adjacent_list[node]:
        if seen[i] and (not visited[i]):
            print(-1)
            exit()
        check(i)
    visited[node] = True
def dfs_path(node):
    if not adjacent_list[node]:
        return 1
    if finish[node]:
        return finish[node]
    tmp = 0
    for i in adjacent_list[node]:
        tmp = max(tmp, dfs_path(i) + 1)
    finish[node] = tmp
    return finish[node]
finished = set()
finish = [0 for i in range(n*(n-1)//2)]
for i in range(n*(n-1)//2):
    check(i)
    dfs_path(i)
print(max(max(finish), 1))
