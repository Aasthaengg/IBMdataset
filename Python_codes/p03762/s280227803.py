N,M = map(int,input().split())
MOD=10**9+7
X=list(map(int,input().split()))
Y=list(map(int,input().split()))

Xsum=0
for i in range(1,N+1):
    Xsum+=X[i-1]*i-(N-i+1)*X[i-1]
    Xsum%=MOD

Ysum=0
for i in range(1,M+1):
    Ysum+=Y[i-1]*i-(M-i+1)*(Y[i-1])
    Ysum%=MOD

print(Xsum*Ysum%MOD)
