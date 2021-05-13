import heapq
N,C = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
X.insert(0,[0,0])
A = [0 for _ in range(N+1)]
for i in range(1,N+1):
    A[i] = A[i-1]+X[i][1]
A = [A[i]-X[i][0] for i in range(N+1)]
B = [0 for _ in range(N+1)]
B[N] = X[N][1]
for i in range(N-1,0,-1):
    B[i] = B[i+1]+X[i][1]
B = [B[i]-(C-X[i][0]) for i in range(N+1)]
heap = []
for i in range(1,N+1):
    heapq.heappush(heap,(-B[i],i))
vmax = 0
for i in range(1,N):
    cnt = A[i]
    vmax = max(vmax,cnt)
    cnt -= X[i][0]
    b,j = heap[0]
    while heap and j<=i:
        heapq.heappop(heap)
        if heap:
            b,j = heap[0]
    b = -b
    cnt += b
    vmax = max(vmax,cnt)
vmax = max(vmax,A[N])
heap = []
for i in range(1,N+1):
    heapq.heappush(heap,(-A[i],i))
for i in range(N,1,-1):
    cnt = B[i]
    vmax = max(vmax,cnt)
    cnt -= (C-X[i][0])
    b,j = heap[0]
    while heap and j>=i:
        heapq.heappop(heap)
        if heap:
            b,j = heap[0]
    b = -b
    cnt += b
    vmax = max(vmax,cnt)
vmax = max(vmax,B[1])
print(vmax)