def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p
    else:
        return (x*pow(x,m-1))%p
p = 10**9+7
N = (2*10**6)//3
A = [1 for _ in range(N+1)]
for i in range(2,N+1):
    A[i] = (A[i-1]*i)%p
B = [1 for _ in range(N+1)]
B[N] = pow(A[N],p-2)
for i in range(N-1,1,-1):
    B[i] = ((i+1)*B[i+1])%p
X,Y = map(int,input().split())
if (X+Y)%3==0 and (X+Y)//3<=X<=2*(X+Y)//3:
    n = (X+Y)//3
    ans = (A[n]*B[X-n])%p
    ans = (ans*B[2*n-X])%p
    print(ans)
else:
    print(0)