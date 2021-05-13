from decimal import Decimal

N,K = map(int,input().split())
A = list(map(int,input().split()))
mod = 10 ** 9 + 7
ans = 0
cnt = 0

def tosa(a,n,d):
    s = Decimal(n / 2) * (2*a+(n-1)*d)
    return int(s)

if N == 1:
    print(ans)
    exit()

for i in range(N-1):
    for j in range(i+1,N):
        if A[i] == A[j]:
            cnt += 1
        if A[i] > A[j]:
            ans += 1

d = N*(N-1)//2
print(tosa(ans,K,d-cnt)%mod)