from collections import deque

n = int(input())
ed = [[] for _ in range(n)]
al,be = [],[]
for _ in range(n-1):
    a,b = map(int,input().split())
    al.append(a-1)
    be.append(b-1)
    ed[a-1].append(b-1)
    ed[b-1].append(a-1)
    
c = list(map(int,input().split()))
c.sort(reverse = True)

ans = [0]*n

q = deque()
q.append(0)
used = [False]*n
used[0] = True
ans[0] = c[0]
j = 1
 
while q:
    p = q.popleft()
    for i in ed[p]:
        if not used[i]:
            used[i] = True
            ans[i] = c[j]
            j += 1
            q.append(i)
        
sc = 0
for i in range(n-1):
    sc += min(ans[al[i]],ans[be[i]])
    
print(sc)
print(*ans)