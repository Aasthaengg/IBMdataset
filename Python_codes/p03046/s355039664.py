M,K=map(int,input().split())
if M==0:
    if K==0:
        print(0,0)
    else:
        print(-1)
elif M==1:
    if K==0:
        print(0,0,1,1)
    else:
        print(-1)
else:
    if K>=2**M:
        print(-1)
    else:
        ans=[]
        for i in range(0,2**M):
            if i!=K:
                ans.append(i)
        ans.append(K)
        for i in range(2**M-1,-1,-1):
            if i!=K:
                ans.append(i)
        ans.append(K)
        print(*ans)