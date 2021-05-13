N, K = map(int, input().split())
A = list(map(int, input().split()))

c = [0] * N
d = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            c[i] += 1

    for j in range(i):
        if A[i] > A[j]:
            d[i] += 1

x = sum(c)
y = x + sum(d)
ans = (K * x + (K * (K - 1) // 2) * y) % (10**9 + 7)

print(ans)
