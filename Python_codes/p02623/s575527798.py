N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    A[i] += A[i-1]
for i in range(1, M+1):
    B[i] += B[i-1]

ans = 0

b_index = M

for a_index in range(N+1):
    left = K - A[a_index]
    if left < 0: continue

    while left - B[b_index] < 0:
        b_index -= 1

    ans = max(ans, a_index + b_index)

print(ans)