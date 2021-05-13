from collections import deque

N,K = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)
    
mod = 10**9+7
L = [0]*N
L[0] = K
ans = 1
q = deque()
q.append(0)
while q:
    t = q.popleft()
    c = max(K-1, L[t])
    for e in E[t]:
        if L[e] == 0:
            c -= 1
            if c <= 0:
                ans = 0
                q = []
                break
            L[e] = c
            q.append(e)
            
for i in range(N):
    ans *= L[i]
    ans %= mod
    
print(ans)