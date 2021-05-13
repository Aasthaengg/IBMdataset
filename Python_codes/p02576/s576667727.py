N,X,T=list(map(int,input().split()))
S=N//X
if N==S*X:
    print(S*T)
else:
    print((S+1)*T)