N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9+7

ans = 0
for i in range(N):
    left = 0
    right = 0
    for j in range(N):
        if(i > j and A[i] > A[j]):
            left += 1
        if(j > i and A[i] > A[j]):
            right += 1
    ans += right*((K+1)*K)//2+(left*(K*(K-1)))//2
print(ans%mod)