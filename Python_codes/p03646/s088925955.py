K = int(input())
N = 50
q, r = divmod(K, N)
A = [N + q - r - 1] * (N - r) + [N + q + N - r] * (r)
print(N)
print(*A)