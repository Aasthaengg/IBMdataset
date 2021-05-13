N, M, C = (int(x) for x in input().split())
b=list(map(int,input().split()))
ans=0

for i in range(N):
    sum=C
    a=list(map(int,input().split()))
    for j in range(M):
        sum+=a[j]*b[j]
    
    if sum>0: ans+=1

print(ans)