MOD = 10 ** 9 + 7
N = int(input())
C = [0] * (N + 1)
for i in range(2, N+1):
    k = i
    for j in range(2, i+1):
        while k % j == 0:
            k //= j
            C[j] += 1
        if k == 1:
            break
ans = 1
for c in C:
    ans *= (c + 1)
    ans %= MOD
print(ans)