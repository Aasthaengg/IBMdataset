N, K, *A = map(int, open(0).read().split())

cntr = [0]*N
cntl = [0]*N


for i, a in enumerate(A):
    l = r = 0
    for b in A[:i]:
        if a > b:
            l += 1
    for b in A[i+1:]:
        if a > b:
            r += 1
    cntr[i] = r
    cntl[i] = l+r

mod = 10**9 + 7
ans = 0
for r in cntr:
    x = r * K % mod
    ans = (ans + x) % mod

c2 = K*(K-1)//2
for l in cntl:
    x = l*c2%mod
    ans = (ans + x) % mod

print(ans)