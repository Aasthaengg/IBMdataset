N, K = map(int, input().split())

M = N*(N-1)//2-K


if M < N-1:
    print(-1)
    exit()

print(M)
for i in range(1, N):
    for j in range(i+1, N+1):
        print(i, j)
        M -= 1
        if M == 0:
            exit()
