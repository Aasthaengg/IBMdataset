X=[0]*60
M=10**9+7
N=int(input())
T=500000004

A=list(map(int,input().split()))

for a in A:
    for k in range(60):
        X[k]+=a%2
        a>>=1


Y=0
y=1
for b in X:
    Y+=b*(N-b)*y
    Y%=M
    y<<=1
print(Y)
