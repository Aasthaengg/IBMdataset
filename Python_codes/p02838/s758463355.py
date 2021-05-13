MOD = 10**9 + 7
N = int(input())
A = list(map(int, input().split()))
ans = 0

for k in range(60):
    count1 = 0
    for i in range(N):
        if (A[i]>>k) & 1:
            count1 += 1
    count0 = N-count1
    ans = (ans + count0*count1*2**k) % MOD

print(ans)