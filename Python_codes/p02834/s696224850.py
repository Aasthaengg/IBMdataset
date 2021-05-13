N,u,v=map(int, input().split())
G=[[] for _ in range(N)]

for i in range(N-1):
    a,b=map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)



from collections import deque

q=deque([])
q.append((v-1,0))
done1=[-1]*N

while q:
    now, dist = q.popleft()
    done1[now]=dist
    for i in G[now]:
        if done1[i]!=-1:
            continue
        q.append((i,dist+1))

q=deque([])
q.append((u-1,0))
done2=[-1]*N

while q:
    now, dist = q.popleft()
    done2[now]=dist
    for i in G[now]:
        if done2[i]!=-1:
            continue
        q.append((i,dist+1))

goal=0
for i in range(N):
    if done1[i]>done2[i]:
        goal=max(goal, done1[i])

ans=goal-1
#print(goal, done1[u-1], done2[v-1])
#print(done1, done2)
print(ans)