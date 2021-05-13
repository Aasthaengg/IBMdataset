import sys
sys.setrecursionlimit(10**6)
n, q = map(int, input().split())
lis = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    lis[a].append(b)
    lis[b].append(a)
c_plus = [0 for _ in range(n)]
for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    c_plus[p] += x
ans = [-1 for _ in range(n)]
def dfs(inp):
    now = inp[0]
    count = inp[1]
    count += c_plus[now]
    ans[now] = count
    for next in lis[now]:
        if ans[next] == -1:
            dfs([next, count])
dfs([0,0])
for i in range(n):
    ans[i] = str(ans[i])
print(" ".join(ans))