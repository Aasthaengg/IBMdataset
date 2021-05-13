N,M=map(int,input().split())
B=[0]*(N+1)
for _ in range(M):
    u,v=map(int,input().split())
    B[u]+=1
    B[v]+=1

for a in range(1,N+1):
    print(B[a])
