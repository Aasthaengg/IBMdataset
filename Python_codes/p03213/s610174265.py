def c(n, P):
    return sum([1 for p in P if p + 1 >= n])


N = int(input())
pN = {}
for i in range(N + 1):
    for j in range(2, i + 1):
        while i % j == 0:
            i //= j
            pN[j] = pN.get(j, 0) + 1
V = pN.values()
ans = c(75, V)
ans += c(25, V) * (c(3, V) - 1)
ans += c(15, V) * (c(5, V) - 1)
ans += c(5, V) * (c(5, V) - 1) * (c(3, V) - 2) // 2
print(ans)
