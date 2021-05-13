from collections import deque

N,M = map(int,input().split())

data = [[] for _ in range(N)]

for i in range(M):
    a,b = map(lambda x:int(x)-1,input().split())
    data[a].append(b)
    data[b].append(a)

q = deque([(0,0)])
ans = [-1]*N

#print(data)

while q:
    x = q.popleft()
    for y in data[x[1]]:
        if y == x[0]:
            continue
        if ans[y] == -1:
            ans[y] = x[1]
            q.append((x[1],y))
    #print(x,q,ans)

if -1 in ans[1:]:
    print('No')
else:
    print('Yes')
    for i in range(1,N):
        print(ans[i]+1)
