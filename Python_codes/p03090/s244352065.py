N = int(input())
M = N * (N - 1) // 2 - N // 2
S = N // 2 * 2 + 1

print(M)

for i in range(1, N):
    for j in range(i + 1, N + 1):
        if i + j == S:
            continue
        print(i, j)