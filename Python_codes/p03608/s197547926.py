n,m,r=map(int,input().split())
r=list(map(int,input().split()))

import sys
INF=float('inf')

road=[[INF]*n for _ in range(n)]

for _ in range(m):
    a,b,c=map(int,input().split())
    road[a-1][b-1]=c
    road[b-1][a-1]=c

#経由地
for k in range(n):
    #出発地
    for s in range(n):
        #goal
        for g in range(n):
            road[s][g]=min(road[s][g],road[s][k]+road[k][g])

import itertools
rlist=list(itertools.permutations(r))

result=10**9
for item in rlist:
    tmp=0
    from_town=item[0]
    for to_town in item[1:]:
        tmp+=road[from_town-1][to_town-1]
        from_town=to_town
    result=min(result,tmp)

print(result)



