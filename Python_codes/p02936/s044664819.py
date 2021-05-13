from collections import deque
n,q = map(int,input().split())
ki = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    ki[a-1].append(b-1)
    ki[b-1].append(a-1)
score = [0 for i in range(n)]

for i in range(q):
    p,x = map(int,input().split()) 
    score[p-1] += x

#print(ki,score)
ans = [0 for i in range(n)]

ans[0] = score[0]
visited = [False]*n
visited[0] = True
Q = deque([0])

while Q:
    d = Q.pop()
    #print(d)
    for to in ki[d]:
        if visited[to]:
            continue
        
        ans[to] = ans[d] + score[to]
        #print(ans[to],ans[d],score[to],d)
        visited[to] = True
        Q.append(to)
print(*ans)