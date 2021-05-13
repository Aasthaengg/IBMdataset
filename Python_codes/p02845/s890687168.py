N, *A = map(int, open(0).read().split())

MOD = 10 ** 9 + 7
ctr = [0] * 3
ans = 1
for a in A:
    ans *= sum(a == v for v in ctr)
    for j in range(3):
        if ctr[j] == a:
            ctr[j] += 1
            break

print(ans % MOD)
