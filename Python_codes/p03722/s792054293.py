N, M = map(int,input().split())
side = [[]for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    side[a-1].append([b-1,c])
node = [-float('inf')]*N
node[0] = 0
for _ in range(N):
    for i in range(N):
        for b,c in side[i]:
            node[b] = max(node[b],node[i]+c)


for _ in range(N):
    for i in range(N):
        for b,c in side[i]:
            if node[b] < node[i]+c:
                node[b] = float('inf')
print(node[-1])