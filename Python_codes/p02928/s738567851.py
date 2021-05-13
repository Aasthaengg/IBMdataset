N,K = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
MOD = 10**9+7
for i in range(N):
    l = 0
    r = 0
    for j in range(N):
        if i<j:
            if A[i]>A[j]:
                r += 1
            else:
                pass
        elif i>j:
            if A[i]>A[j]:
                l += 1
            else:
                pass
    ans += l*max(0,(K-1)*(K)//2)
    ans %= MOD
    ans += r*(K+1)*K//2
    ans %= MOD
print(ans)