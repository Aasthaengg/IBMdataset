N,X,Y=map(int,input().split())

if Y<X:
    X,Y=Y,X

Dist=[0 for i in range(N)]

for i in range(1,N):
    for j in range(i,N+1):
        dist_a=j-i
        dist_b=abs(i-X)+abs(j-Y)+1
        ans=min(dist_a,dist_b)
        Dist[ans]+=1

for i in range(1,N):
    print(Dist[i])