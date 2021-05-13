N,K = map(int,input().split())

MAXK = int((N-1)*(N-2)/2)

if K > MAXK:
    print(-1)
    exit()

edge = []

# スターを作成
for i in range(2,N+1):
    edge.append([1,i])

now = 2
node = now + 1
for _ in range(MAXK - K):
    edge.append([now,node])
    node += 1
    if node > N:
        now += 1
        node = now + 1

M = len(edge)
print(M)
for u,v in edge:
    print(u,v)