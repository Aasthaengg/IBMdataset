N = int(input())

print(N * (N-1) // 2 - N // 2)
M = 1 if N % 2 == 0 else 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if j == N + M - i:
            continue
        print(i,j)
