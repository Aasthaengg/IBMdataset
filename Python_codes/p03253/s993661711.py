N, M = map(int, input().split())
if N == 1 or M == 1:
    print(1)
    exit()
MOD = 10**9+7
A = []
m = M
for i in range(2, int(M**0.5)+1):
    if m % i == 0:
        m //= i
        k = 1
        while m % i == 0:
            m //= i
            k += 1
        A.append(k)
        if m == 1:
            break
else:
    A.append(1)
B = [0] * max(A)
for a in A:
    B[a-1] += 1
fn_1 = 1
for i in range(1, N):
    fn_1 *= i
    fn_1 %= MOD
ans = 1
fk = fn_1
for i, b in enumerate(B, N):
    fk *= i
    fk %= MOD
    fk *= pow(max(1, i - N + 1), MOD-2, MOD)
    fk %= MOD
    ans *= pow(fk, b, MOD)
    ans %= MOD
    ans *= pow(pow(fn_1, b, MOD), MOD-2, MOD)
    ans %= MOD
print(ans)