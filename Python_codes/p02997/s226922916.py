import sys
N,K=map(int,input().split())
if K>(N-1)*(N-2)//2:
    print(-1)
    sys.exit()

k=(N-1)*(N-2)//2
G=[]
for i in range(2,N+1):
    G.append([1,i])

s,g=2,3
while k!=K:
    G.append([s,g])
    g+=1
    if g==N+1:
        s+=1
        g=s+1
    k-=1

print(len(G))
for i in G:
    print(*i)