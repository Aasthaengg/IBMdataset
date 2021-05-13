from sys import stdin, setrecursionlimit as srl
from threading import stack_size
srl(int(1e9)+7)
stack_size(int(1e8))

def get(i, value, vis):
    if vis[i]:
        return value[i]
    vis[i] = True
    ans = 0
    for j in adj[i]:
        ans = max(ans, 1+get(j, value, vis))
    value[i] = ans
    return ans


n, m = map(int, input().split())
adj = {}
for i in range(n):
    adj[i] = []
for i in range(m):
    x, y = map(int,input().split())
    adj[x-1].append(y-1)
vis = [False for i in range(n)]
value = [0 for i in range(n)]
for i in range(n):
    value[i] = get(i, value, vis)
x = 0
for i in value:
    x = max(x, i)
print(x)
