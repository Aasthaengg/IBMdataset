K = int(input())
N = 50
p = (K - 1) // N
r = (K - 1) % N + 1
ans = [2 * N + p - r] * r + [N + p - r - 1] * (N - r)
print(N)
print(*ans)
