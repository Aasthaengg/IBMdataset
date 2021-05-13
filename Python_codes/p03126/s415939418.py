N,M=map(int,input().split())
m=[0]*M
for i in range(N):
    k=list(map(int,input().split()))
    for a in k[1:]:
        m[a-1]+=1
print(m.count(N))