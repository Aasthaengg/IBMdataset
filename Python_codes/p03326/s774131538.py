n,m=map(int,input().split())

xyz=[tuple(map(int, input().split())) for _ in range(n)]
kk=[]
for i in [1,-1]:
    for j in [1,-1]:
        for k in [1,-1]:
            kk.append((i,j,k))

ans=[[] for _ in range(8)]

for (x,y,z) in xyz:
    for i,k in enumerate(kk):
        ans[i].append(x*k[0]+y*k[1]+z*k[2])

result=0

for i in range(8):
    ans[i].sort(reverse=True)
    #print(sum(ans[i][:m]))
    result=max(result,sum(ans[i][:m]))

print(result)



