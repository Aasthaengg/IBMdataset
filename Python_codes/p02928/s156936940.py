N,K = map(int,input().split())
A = list(map(int,input().split()))
MOD = 10**9+7

inv = 0
for i in range(N-1):
    for j in range(i+1,N):
        if A[i] > A[j]:
            inv += 1
ans = (inv * K) % MOD

from collections import Counter
ctr = Counter(A)
inv2 = 0
s = 0
for _,v in sorted(ctr.items()):
    inv2 += v * s
    s += v
ans += inv2 * K*(K-1)//2
ans %= MOD
print(ans)