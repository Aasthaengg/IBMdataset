import sys,collections
input = sys.stdin.readline

N,Q = list(map(int,input().split()))
road = [[] for i in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    road[a].append(b)
    road[b].append(a)
point = [0]*(N+1)

for _ in range(Q):
    p,x = map(int,input().split())
    point[p] += x

q = collections.deque([1])
visit = [0]*(N+1)
visit[1]=1

while q:
    now = q.pop()
    for i in road[now]:
        if visit[i] == 0:
            q.append(i)
            point[i] += point[now]
            visit[i]=1

print(*point[1:])
