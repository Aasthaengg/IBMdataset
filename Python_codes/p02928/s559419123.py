N,K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

after_sum = 0
whole_sum = 0
for i in range(N):
    before = 0
    after = 0
    for j in range(N):
        if A[i] > A[j]:
            if i < j:
                after += 1
            elif j < i:
                before += 1
    # print(before, after)
    whole = before + after
    after_sum = (after_sum + after) % MOD
    whole_sum = (whole_sum + whole) % MOD

a = (K * after_sum) % MOD
b = ((K - 1) * K // 2) % MOD
b = (b * whole_sum) % MOD
print((a + b) % MOD)
