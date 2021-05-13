import heapq
X,Y,Z,K = map(int,input().split())
A = sorted(list(map(int,input().split())),reverse=1)
B = sorted(list(map(int,input().split())),reverse=1)
C = sorted(list(map(int,input().split())),reverse=1)
Q = [(-A[0]-B[0]-C[0],0,0,0)]
heapq.heapify(Q)
abc = [(0,0,0)]
for i in range(K):
    n,a,b,c = heapq.heappop(Q)
    if a < X-1 and (a+1,b,c) not in abc:
        abc.append((a+1,b,c))
        heapq.heappush(Q,(n+A[a]-A[a+1],a+1,b,c))
    if b < Y-1 and (a,b+1,c) not in abc:
        abc.append((a,b+1,c))
        heapq.heappush(Q,(n+B[b]-B[b+1],a,b+1,c))
    if c < Z-1 and (a,b,c+1) not in abc:
        abc.append((a,b,c+1))
        heapq.heappush(Q,(n+C[c]-C[c+1],a,b,c+1))
    print(-n)