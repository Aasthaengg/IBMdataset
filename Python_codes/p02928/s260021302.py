N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7
inner_cnt = 0
outer_cnt = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            outer_cnt += 1
            if j > i:
                inner_cnt += 1
ans = inner_cnt * K
ans %= MOD
ans += outer_cnt * K * (K - 1) // 2
ans %= MOD
print(ans)
