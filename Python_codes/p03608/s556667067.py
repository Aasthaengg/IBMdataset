import itertools


N,M,R = map(int,input().split())
r = list(map(int,input().split()))
INF = float('inf')
D = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    D[i][i] = 0

for _ in range(M):
    a,b,c = map(int,input().split())
    D[a][b] = c
    D[b][a] = c

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

loads = list(itertools.permutations(r))
# for load in loads:
#     print(load)
ans = INF
#ans_load = None
for load in loads:
    temp = 0
    for i in range(R-1):
        temp += D[load[i]][load[i+1]]
    #print(load,temp)
    ans = min(temp,ans)
    # if temp < ans:
    #     ans = temp
    #     ans_load = load

print(ans)
#print(ans_load)