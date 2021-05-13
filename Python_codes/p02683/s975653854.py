number=list(map(int,input().split()))
N,M,X=number[0],number[1],number[2]
price=0
nums=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    nums.append(tmp)
target=[0 for i in range(M)]
answer=10000000
for cowmask in range(1<<N):
        price=0
        target=[0 for k in range(M)]
        for x in range(N):
                if (cowmask>>x)&1==0:
                    price+=nums[x][0]
                    for j in range(1,M+1):
                        target[j-1]+=nums[x][j]
        if min(target)>=X:
            answer=min(answer,price)

if answer==10000000:
    print(-1)
else:
    print(answer)