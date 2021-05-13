n, k = map(int, input().split())
A = list(map(int, input().split()))
ans1 = 0
ans2 = 0
mod = 10 ** 9 + 7
for i, a in enumerate(A):
    for j, b in enumerate(A):
        if a > b:
            if i < j:
                ans1 += 1
                ans2 += 1
            else:
                ans2 += 1

print(((ans1 * k) % mod + ((ans2 * ((k * (k - 1)) // 2) % mod)) % mod) % mod)

