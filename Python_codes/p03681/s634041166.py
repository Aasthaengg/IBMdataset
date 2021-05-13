p = 10**9+7
N,M = map(int,input().split())
A = [1 for _ in range(N+1)]
for i in range(2,N+1):
    A[i] = (i*A[i-1])%p
B = [1 for _ in range(M+1)]
for i in range(2,M+1):
    B[i] = (i*B[i-1])%p
if abs(N-M)>1:
    ans = 0
elif abs(N-M)==1:
    ans = (A[N]*B[M])%p
elif abs(N-M)==0:
    ans = (2*A[N]*B[M])%p
print(ans)