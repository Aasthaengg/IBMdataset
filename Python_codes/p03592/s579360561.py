N,M,K=map(int, input().split())
#最初しろ
#行、列ごとに反転
L=[0]*(10**7)
if K==0 or K==N*M:
    print("Yes")
else:
    for h in range(N+1):
        for w in range(M+1):
            now=h*w+(N-h)*(M-w)
            L[now]+=1
    if L[K]>0:
        print("Yes")
    else:
        print("No")


