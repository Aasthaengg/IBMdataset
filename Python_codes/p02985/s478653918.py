import sys
input = sys.stdin.readline
from collections import deque

mod = 10**9 + 7

n,k = map(int,input().split())
if(n == 1):
    print(k)
    exit()


edges = {}
d = [0] * (n+1)
for i in range(1,n+1):
    edges[i] = []

for i in range(n-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)
    d[a] += 1
    d[b] += 1

for i in range(1,n+1):
    if(d[i] == 1):
        first = i
        break

d = [0] * (n+1)
d[0] = -1
d[first] = -1
dq = deque()
dq.appendleft([0,first])

ans = 1
while(len(dq) > 0):
    parent, child = dq.pop()
    d[parent] += 1
    d[child] += 1
    ans = ans * (k - d[parent]) % mod

    for i in edges[child]:
        if(i != parent):
            dq.appendleft([child, i])

print(ans)