from collections import deque
n,q = map(int,input().split())
l =  [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    l[a].append(b)
    l[b].append(a)

value = [0 for _ in range(n)]
for _ in range(q):
    p,q = map(int,input().split())
    value[p-1] += q

bit = [0 for _ in range(n)]
"""
def dfs(k):
    bit[k] = 1
    for i in l[k]:
        if bit[i]==0:
            value[i] += value[k]
            dfs(i)
"""
d = deque([0])
while d:
    a = d.popleft()
    bit[a] = 1
    for i in l[a]:
        if bit[i]==0:
            d.append(i)
            value[i] += value[a]
        

print(*value)
