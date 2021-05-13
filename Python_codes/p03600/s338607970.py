n=int(input())
inf=10**15
a=[[0]*n for _ in range(n)]
dist=[[0]*n for _ in range(n)]

for u in range(n):
    for v,c in enumerate(list(map(int,input().split()))):
        a[u][v]=c
        dist[u][v]=c

def calc(n,a,dist):

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if k==i or k==j or i==j or dist[i][k]==inf or dist[k][j]==inf:
                    continue
                
                if dist[i][k]+dist[k][j]==a[i][j]:
                    dist[i][j]=inf
                elif dist[i][k]+dist[k][j]<a[i][j]:
                    return -1
    
    ret=0
    for i in range(n):
        for j in range(n):
            if dist[i][j]==inf:
                continue
            ret+=dist[i][j]
    
    return ret//2


print(calc(n,a,dist))