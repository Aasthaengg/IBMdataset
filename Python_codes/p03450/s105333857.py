import sys
import io
import math
import string
# solution

sys.setrecursionlimit(100001)
def input():
    return sys.stdin.readline()[:-1]

def dfs(v):
    ret = True
    for u, d in es[v]:
        if x[u] == None:
            x[u] = x[v] + d
            ret = ret and dfs(u)
        elif x[u] != x[v] + d:
            return False
    return ret

N, M = map(int, input().split())
es = [[] for i in range(N+1)]
for i in range(M):
    L, R, D = map(int, input().split())
    es[L].append((R, D))
    es[R].append((L, -D))
x = [None for i in range(N+1)]
flag = True
for v in range(1, N+1):
    if x[v] == None:
        x[v] = 0
        if dfs(v) == False:
            flag = False
            break
if flag:
    print("Yes")
else:
    print("No")