from collections import defaultdict,deque
def hash(x,y):
    x,y =min(x,y),max(x,y)
    return x*(N+1)+y
s = set()
N = int(input())
edge = [[] for _ in range(N*N+N)]
ind = [0]*(N*N+N)
for i in range(1,N+1):
    A = list(map(int,input().split()))
    s.add(hash(i,A[0]))
    for j in range(N-2):
            edge[hash(i,A[j])].append(hash(i,A[j+1]))
            ind[hash(i,A[j+1])] += 1
d = deque()
nd = deque()
for hash in s:
    if ind[hash] == 0:
        d.append(hash)
ans = 0
finished = 0
while d:
    while d:
        hash = d.popleft()
        finished += 1
        for nhash in edge[hash]:
            ind[nhash] -= 1
            if ind[nhash] == 0:
                nd.append(nhash)
    d = nd
    nd = deque()
    ans += 1
if finished == N*(N-1)//2:
    print(ans)
else:
    print(-1)