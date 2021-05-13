N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9 + 7

# そもそも超えている
already = 0
for i in range(N):
    for j in range(i + 1, N):
        if (i == j):
            continue
        if (A[i] > A[j] and i < j):
            already += 1
already_count = already * K

L = []
L.extend(A)
L.extend(A)
count = 0
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if (i == j):
            continue
        if (L[i] > L[j] and i < j):
            count += 1
inc = count - (already * 2)

tousa_sum = ((K - 1) * (1 + (K - 1))) // 2
print((inc * tousa_sum + already_count) % mod)
