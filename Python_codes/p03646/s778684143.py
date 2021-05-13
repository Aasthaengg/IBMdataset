K = int(input())
N = 50
p, r = divmod(K, N)
ans = [2 * N + p - r] * r + [N + p - r - 1] * (N - r)
print(N)
print(*ans)
