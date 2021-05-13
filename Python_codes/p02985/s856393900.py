from collections import deque
import sys
sys.setrecursionlimit(10++7)

n,k = map(int,input().split())
E = [[] for i in range(n)]
for i in range(n-1):
    
    a,b = map(int,input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

mod = 10**9+7

ans = k
q = deque([])
i = 1
for nex in E[0]:
    ans *= k-i
    ans %= mod
    i += 1
    q.append((nex,0))

while q:
    now,bef =  q.popleft()
    i = 2
    for nex in E[now]:
        if nex == bef:
            continue
        ans *= k-i
        ans %= mod
        i += 1
        q.append((nex,now))
print(ans)
