K = int(input())

N = 50
ans = [K // N + N] * (K % N) + [K // N + N - K % N - 1] * (N - K % N)
print(N)
print(*ans)
