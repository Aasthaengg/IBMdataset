N, M = map(int, input().split())

if N > M:
    N, M = M, N

if N == 1:
    if M == 1:
        print(1)
        exit()
    else:
        M -= 2
else:
    N -= 2
    M -= 2

print(N * M)
