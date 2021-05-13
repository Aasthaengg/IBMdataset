import collections
N,C=map(int,input().split())
cost=[list(map(int,input().split())) for _ in range(C)]
table=[list(map(int,input().split())) for _ in range(N)]
l=[[] for _ in range(3)]
costs=[[] for _ in range(3)]

for i in range(N):
    for j in range(N):
        l[(i+j)%3].append(table[i][j])
#print(l)
c1=collections.Counter(l[0])
c2=collections.Counter(l[1])
c3=collections.Counter(l[2])
costs=[[] for _ in range(3)]
for i in range(C):
    for j in range(3):
        buf=0
        for k in l[j]:
            buf=buf+cost[k-1][i]
        costs[j].append(buf)
#print(costs)
mi=float("inf")
for i in range(C):
    for j in range(C):
        for k in range(C):
            if (i!=j)and(j!=k)and(i!=k):
                mi=min(mi,costs[0][i]+costs[1][j]+costs[2][k])
print(mi)