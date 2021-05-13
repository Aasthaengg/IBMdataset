n, k = map(int,input().split())
A = list(map(int, input().split()))
mod = 10**9+7

if n == 1:
    print(0)
    exit()

ans = 0
for i in range(n-1):
    for j in range(i, n):
        if A[i] < A[j]:
            ans += (k-1)*k//2
        elif A[i] > A[j]:
            ans += k*(k+1)//2
        else:
            pass
        ans %= mod
print(ans)
