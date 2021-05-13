N, K = map(int, input().split())
A = list(map(int, input().split()))
max_a = max(A)
MOD = 10**9 + 7

memo = [0] * (max_a + 1)
num = 0
for a in A:
    memo[a] += 1
    num += sum(memo[a+1:])

num_larger = 0
for a in A:
    num_larger += sum(memo[a+1:])

ans = ((num*K % MOD) + ((K*(K-1)//2)*num_larger) % MOD) % MOD
print(ans)