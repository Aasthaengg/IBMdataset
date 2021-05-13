n,m,x=map(int,input().split())
A=[]
for i in range(n) :
    A.append(list(map(int,input().split())))

cost=2*10**6
count=0
for i in range(2**n) :    #参考書の買う場合の数
    cost1=0
    B=[[] for i in range(m)]
    for j in range(n) :   #どの本を買うか
        if ((i>>j)&1) :
            cost1+=A[j][0]
            for k in range(1,m+1) :
                B[k-1].append(A[j][k])

    for k in range(m) :
        if x<=sum(B[k]) :
            continue
        else :
            count+=1
            break
    else :
        cost=min(cost,cost1)
            
if count==2**n :
    print(-1)
else :
    print(cost)    