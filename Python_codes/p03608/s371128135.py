from collections import deque
import itertools
INF = 10**12+7
N,M,R = map(int,input().split())
r = list(map(int,input().split()))
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
for i in itertools.permutations(r,len(r)):
    val = 0
    for j in range(1,len(r)):
        val += d[i[j-1]][i[j]]
    ans = min(ans,val)
print(ans)

    
