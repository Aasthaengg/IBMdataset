N,K = list(map(int,input().split()))
A = list(map(int,input().split()))

ans = 0
mod = 10**9+7

for n in range(N):
    for i in range(N):
        if A[n] > A[i]:
            if n<i:ans += (K*(K+1)//2)%mod
            else:ans+=(K*(K-1)//2)%mod

print(ans%mod)
