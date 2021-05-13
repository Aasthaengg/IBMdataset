N,K=map(int,input().split())
if K<=((N-1)*(N-2))//2:
    G = {i:[] for i in range(1,N+1)}
    for i in range(1,N+1):
        for j in range(1,N+1):
            if j!=i:
                G[i].append(j)
    cnt = 0
    for i in range(2,N+1):
        for j in range(2,N+1):
            if j in G[i]:
                if cnt==K:break
                G[i].remove(j)
                G[j].remove(i)
                cnt += 1
        if cnt==K:break
    print((N*(N-1))//2-K)
    for i in range(1,N):
        for j in G[i]:
            if j>i:
                print(i,j)
else:
    print(-1)