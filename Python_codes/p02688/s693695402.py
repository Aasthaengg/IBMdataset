N,K=map(int,input().split())
D=[]
A=[]
DB=[0]*N

for k in range(K):
    D.append(int(input()))
    A.append(list(map(int,input().split())))

for a in A:
    for i in a:
        DB[i-1]+=1

ans=0

for db in DB:
    if db==0:
        ans+=1

print(ans)