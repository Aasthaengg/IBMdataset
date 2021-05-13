N,K=map(int,input().split())
if N%K==0:
    print(0)
else:
    a=N%K
    b=abs(a-K)
    if a<b:
        print(a)
    else:
        print(b)