N,M,C=map(int,input().split())
B=list(map(int,input().split()))
Ai= [input().split() for l in range(N)]
count=0
for i in range(N):
    tot=0
    for j in range(M):
        tot+=int(Ai[i][j])*B[j]
    if tot+C>0:
        count+=1  
print(count)