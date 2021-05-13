N,k = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
MOD = 10**9+7
for i in range(N):
    for j in range(i+1,N):
        if A[i] > A[j]:
            ans += k*(k+1)//2
        elif A[i] < A[j]:
            ans += k*(k-1)//2

        ans %= MOD

print(ans)