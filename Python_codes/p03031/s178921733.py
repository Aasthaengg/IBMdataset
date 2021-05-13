from itertools import product
n,m=map(int,input().split())
ks=[list(map(int,input().split())) for _ in range(m)]
p=list(map(int,input().split()))
count=0
for i in product([0,1],repeat=n):
    for j in range(m):
        
        temp=0
        for k in range(ks[j][0]):
            if i[ks[j][k+1]-1]==1:
                temp+=1
        if temp%2!=p[j]:
            break
    else: 
        count+=1
print(count)
