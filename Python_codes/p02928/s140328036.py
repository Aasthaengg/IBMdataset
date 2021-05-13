n, k = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7
cnt = 0
for _ in range(n):
    for i in range(n-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            cnt += 1
AA = A*2
nn = len(AA)
out_cnt = 0
for _ in range(nn):
    for i in range(nn-1):
        if AA[i] > AA[i+1]:
            AA[i], AA[i+1] = AA[i+1], AA[i]
            out_cnt += 1
ans = (k*cnt % MOD + out_cnt * (k*(k-1)//2) % MOD) % MOD
print(ans)
