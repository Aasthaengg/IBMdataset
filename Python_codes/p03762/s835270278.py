MOD=1000000007
N,M=map(int,input().split())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
XX=[x2-x1 for x2,x1 in zip(X[1:],X[:-1])]
YY=[x2-x1 for x2,x1 in zip(Y[1:],Y[:-1])]

xs = [((i+1)*(N-i-1)*XX[i])%MOD for i in range(N-1)]
totaly=0
for j in range(M-1):
    tmp = ((j+1)*(M-j-1)*YY[j])%MOD
    totaly = (totaly+tmp)%MOD
ans = 0
for x in xs:
    tmp = (totaly*x)%MOD
    ans = (ans+tmp)%MOD

print(ans)
