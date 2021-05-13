M,K=map(int,input().split())
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
    if 0<=K<2**M:
        X=[i^K for i in range(2**M)]+[K]+[i^K for i in range(1,2**M)][::-1]
        print(" ".join([str(i) for i in X]))
    else:
        print(-1)
