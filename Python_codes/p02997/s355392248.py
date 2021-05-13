from itertools import combinations

N,K=list(map(int,input().split()))

node=(N-1)*(N-2)//2

if K>node:
    print(-1)
    exit(0)

g=[[] for _ in range(N+1)]
M=0

for i in range(2,N+1):
    g[1].append(i)
    M+=1

cnt=node-K

for u,v in combinations(range(2,N+1),2):
    if cnt==0:
        break
    g[u].append(v)
    
    M+=1
    cnt-=1


print(M)
for i in range(1,N+1):
    for j in g[i]:
        print('{} {}'.format(i,j))