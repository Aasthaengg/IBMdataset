N,K=map(int,input().split())
a=N//K
if a==0:
    x=N
    y=abs(N-K)
    if x>y:
        print(y)
    else:
        print(x)
elif N%K!=0:
    x=N-a*K
    y=abs(N-(a+1)*K)
    if x>y:
        print(y)
    else:
        print(x)
else:
    print(0)