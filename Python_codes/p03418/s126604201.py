N,K=map(int,input().split())
cnt=0
if K==0:
    print(N*N)
else:
    for i in range(K+1,N+1):    #bの数について
        fin=N%i
        if (fin>=K):
            cnt=cnt+(fin-K)+1
        clus=(N-fin)//i
        cnt=cnt+clus*(i-K)
        #print(cnt)
    print(cnt)