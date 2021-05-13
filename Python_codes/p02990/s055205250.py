p = 10**9+7
def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p
    else:
        return (x*(pow(x,(m-1)//2)**2)%p)%p
N,K = map(int,input().split())
A = [1 for _ in range(N+1)]
for i in range(2,N+1):
    A[i] = (i*A[i-1])%p
B = [1 for _ in range(N+1)]
B[N] = pow(A[N],p-2)
for i in range(N-1,1,-1):
    B[i] = ((i+1)*B[i+1])%p
for i in range(1,K+1):
    if N-K<i-1:
        ans = 0
    else:
        a = A[K-1]
        a = (a*B[K-i])%p
        a = (a*B[i-1])%p
        b = A[N-K+1]
        b = (b*B[N-K+1-i])%p
        b = (b*B[i])%p
        ans = (a*b)%p
    print(ans)