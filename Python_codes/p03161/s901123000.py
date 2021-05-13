N,K=map(int,input().split())


T=list(map(int,input().split()))
S=[10**10]*(10**6)
DP=[10**10]*(10**6)

for i in range(N):
    S[i]=T[i]    

def chmin(a,b):
    if a>b:
        return b
    else:
        return a

def chmax(a,b):
    if a>b:
        return a
    else:
        return b

DP[0]=0
DP[1]=abs(S[1]-S[0])

for i in range(N):
    for j in range(1,K+1):
        DP[i+j]=chmin(DP[i]+abs(S[i+j]-S[i]),DP[i+j])
    
print(DP[N-1])
