N, M = map(int, input().split())

if N < M // 2:
    print((N + M // 2) // 2)
else:
    print(M//2)