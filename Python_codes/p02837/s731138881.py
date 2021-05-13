# ABC 147 C

N=int(input())
A=[[] for _ in [0]*N]
for i in range(N):
    a=int(input())
    for _ in [0]*a:
        A[i].append(tuple(map(int,input().split())))

res=0
for n in range(1<<(N)):
    check=[-1]+[(n>>j)&1 for j in range(N)]
    cnt=0
    j=0
    for j in range(N):
        if check[j+1]==1:
            cnt+=1
            #syouziki
            for x,y in A[j]:
                if check[x] == 1-y:
                    check[0]=1
                if check[0]>0:
                    break
        if check[0]>0:
            break
    if check[0]>0:
        continue
    res=max(res,cnt)
print(res)