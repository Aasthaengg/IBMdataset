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
Z = list(map(int,input().split()))
A = [1 for _ in range(N+1)]
for i in range(2,N+1):
    A[i] = (A[i-1]*i)%p
B = [1 for _ in range(N+1)]
B[N] = pow(A[N],p-2)
for i in range(N-1,1,-1):
    B[i] = (B[i+1]*(i+1))%p
def f(n,k):
    if k>n:
        return 0
    return (A[n]*B[k]*B[n-k])%p
X = sorted(Z,reverse=True)
X.insert(0,0)
ans = 0
for i in range(1,N-K+2):
    ans = (ans+X[i]*f(N-i,K-1))%p
Y = sorted(Z)
Y.insert(0,0)
for i in range(1,N-K+2):
    ans = (ans-Y[i]*f(N-i,K-1))%p
print(ans)