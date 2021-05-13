N,K=map(int,input().split(' '))
if K%2==0:
    cnt_0=0
    cnt_k2=0
    for i in range(1,N+1):
        if i%K==0:
            cnt_0+=1
        if i%K==K//2:
            cnt_k2+=1
    print(cnt_0**3+cnt_k2**3)

else:
    print((N//K)**3)