N, K = map(int, input().split())
mod = 10**9+7
A = list(map(int,input().split()))
cnt1 = 0
cnt2 = 0
for i in range(N):
    for k in range(N):
        if A[i] > A[k]:
            if i+1 <= k < N:
                cnt1 += 1
                cnt2 += 1
            else:
                cnt2 += 1
            cnt1 %= mod
            cnt2 %= mod
#print(cnt1, cnt2)
ans = (cnt1 * K + cnt2 * (K-1)*K // 2) % mod
print(ans)        