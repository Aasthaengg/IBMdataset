def lcm(X,Y):
    x=X
    y=Y
    if y>x:
        x,y=y,x
    while x%y!=0:
        x,y=y,x%y
    return X*Y//y

MOD = 1000000007
N = int(input())
A = list(map(int,input().split()))

LCM = A[0]
for i in range(0,N-1,1):
    LCM = lcm(LCM,A[i+1])
B = [0 for i in range(0,N,1)]
for i in range(0,N,1):
    B[i]= (LCM%MOD)*pow(A[i],MOD-2,MOD)%MOD

ans = 0
for i in range(0,N,1):
    ans = (B[i] + ans)%MOD

print(ans)