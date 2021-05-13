def comb(n, k, mod=10**9+7):
    num = den = 1
    for i in range(k):
        num *= n - i
        den *= i + 1
    return num // den

N, P = map(int, input().split())
A = list(map(int, input().split()))
cnt = [0] * 2
for a in A:
    cnt[a % 2] += 1
even = 0
odd = [0] * 2
for i in range(N+1):
    even += comb(cnt[0], i)
    odd[i % 2] += comb(cnt[1], i)
print(even * odd[P])