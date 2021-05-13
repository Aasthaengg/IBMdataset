from collections import deque
INF = 10**12+7
N,M,R = map(int,input().split())
r = list(map(str,input().split()))
d = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int,input().split())
    d[A][B] = C
    d[B][A] = C
for i in range(1,N+1):
    d[i][i] = 0
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            d[i][j] = min(d[i][j],d[i][k] + d[k][j])
#print(d)
ans = INF
que = deque([])
for i in r:
    que.append([i])
while len(que) != 0:
    p = que.popleft()
    if len(p) == R:
        #print(p)
        val = 0
        for i in range(1,R):
            val += d[ int(p[i-1])][int(p[i])]
        ans = min(ans,val)
    else:
        for i in r:
            if not i in p:
                que.append(p+[i])
print(ans)