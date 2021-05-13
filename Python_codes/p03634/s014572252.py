
from collections import deque
N=int(input())
T=[[] for _ in range(N)]
for i in range(N-1):
    a,b,c=map(int, input().split())
    T[a-1].append((b-1,c))
    T[b-1].append((a-1,c))

Q,K=map(int, input().split())
que=deque([(K-1,0)])
done=[-1]*N
while que:
    t=que.popleft()
    now,nowd=t
    done[now]=nowd
    for nex in T[now]:
        nexnode,nexd=nex
        if done[nexnode]!=-1:
            continue
        else:
            que.append((nexnode, nowd+nexd))

#print(done)
for i in range(Q):
    x,y=map(int, input().split())
    print(done[x-1]+done[y-1])