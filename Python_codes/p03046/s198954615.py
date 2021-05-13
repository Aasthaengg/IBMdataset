M,K=map(int,input().split())
if K==0:
    L=[i for i in range(2**M)]
    L=L+L
    L.sort()
    ans="0"
    for i in range(1,len(L)):
        ans+=" "+str(L[i])
    print(ans)
elif K<2**(M):
    if M==0 or M==1:
        print(-1)
    else:
        A="0 "+str(K)+" 0"
        for i in range(1,2**(M)):
            if i==K:
                pass
            else:
                A+=" "+str(i)
        A+=" "+str(K)
        for i in range(1,2**(M)):
            if (2**(M)-i)==K:
                pass
            else:
                A+=" "+str(2**(M)-i)
        print(A)
else:
    print(-1)