n,m=map(int,input().split())
deg=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    deg[a]+=1
    deg[b]+=1
print(*deg,sep="\n")