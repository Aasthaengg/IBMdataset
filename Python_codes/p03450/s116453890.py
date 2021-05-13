from collections import deque
n,m = map(int,input().split())

path = [[] for _ in range(n)]

for _ in range(m):
    l,r,d = map(int,input().split())
    path[l-1].append((r-1, d))
    path[r-1].append((l-1,-d))

pos = [None] * n

q = deque([0])
not_take = set(range(1,n))

ans = "Yes"

while q:
    
    a = q.popleft()
    if pos[a] is None:
        pos[a] = 0
    
    for b,dx in path[a]:
        
        if pos[b] is None:
            pos[b] = pos[a] + dx
            q.append(b)
            not_take.discard(b)
        elif pos[b] != pos[a] + dx:
            ans = "No"
            break
    if ans == "No": break
        
    if (not q) and (not_take != set()):
        q.append(not_take.pop())

if ans == "Yes" and max(pos) - min(pos) > 1e9:
    ans = "No"

print(ans)