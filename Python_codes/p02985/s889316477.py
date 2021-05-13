import collections
N,K = map(int,input().split())
edge = collections.defaultdict(list)
for _ in range(N-1):
    a,b = map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
q = collections.deque()
q.append((0,-1))
M = K
while q:
    p,root = q.pop()
    if root == -1:
        for k in range(K-1,K-1-len(edge[p]),-1):
            M *= k
            M %= 10 ** 9 + 7
    else:
        for k in range(K-2,K-1-len(edge[p]),-1):
            M *= k
            M %= 10 ** 9 + 7
    for e in edge[p]:
        if e != root:
            q.append((e,p))
print(M)