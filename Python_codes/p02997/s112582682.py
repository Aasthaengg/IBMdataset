N, K = map(int, input().split())
if K> ((N-1)*(N-2))//2:
    print(-1)
else:
    p = []
    q = []
    for t in range(2, N):
        for u in  range(t+1, N+1):
            q.append([t, u])
    for i in range(2, N+1):
        p.append([1, i])
    for j in range(((N-1)*(N-2))//2 - K):
        p.append(q[j])
    print(len(p))
    for y in p:
        print(*y)