n,m=map(int,input().split())
xyz=[list(map(int,input().split())) for i in range(n)]
ans=[]
for i in [-1,1]:
    for j in [-1,1]:
        for k in [-1,1]:
            ans.append(sum(sorted([i*l[0]+j*l[1]+k*l[2] for l in xyz],reverse=True)[:m]))
print(max(ans))