N,M,L=map(int,input().split())
A=[[] for i in range(N)]
for i in range(M):
    a,b,c=map(int,input().split())
    A[a-1].append((b-1,c))
    A[b-1].append((a-1,c))
d=[[100000000001]*N for i in range(N)]
for i in range(N):
    d[i][i]=0
for i in range(N):
    for to,cost in A[i]:
        d[i][to] = cost
for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][k] != 100000000001 and d[k][j] != 100000000001:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
B=[[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if d[i][j]<=L:
            B[i].append((j,1))
times=[[100000000001]*N for i in range(N)]
for i in range(N):
    times[i][i]=0
for i in range(N):
    for to,cost in B[i]:
        times[i][to] = cost
for k in range(N):
    for i in range(N):
        for j in range(N):
            if times[i][k] != 100000000001 and times[k][j] != 100000000001:
                times[i][j] = min(times[i][j], times[i][k] + times[k][j])
Q=int(input())
for i in range(Q):
    s,t=map(int,input().split())
    if times[s-1][t-1]!=100000000001:
    	print(times[s-1][t-1]-1)
    else:
      	print(-1)