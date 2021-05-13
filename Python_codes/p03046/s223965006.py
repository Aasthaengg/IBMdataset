
M,K = list(map(int,input().split()))

if M==0:
    if K==0:
        print("0 0")
    else:
        print(-1)
elif M==1:
    if K==0:
        print("0 0 1 1")
    else:
        print(-1)
else:
    if K==0:
        ans = []
        for i in range(2**M):
            ans.append(i)
            ans.append(i)
        #ans = list(map(str,ans))
        print(*ans)
    elif K<2**M:
        ans = [0,K,0]
        ansc = []
        for i in range(1,2**M):
            if i!=K:
                ansc.append(i)
                
        ans =ans+ansc + [K] +ansc[::-1]
        #ans = list(map(str,ans))
        print(*ans)
    else:
        print(-1)