
N, K = map(int, input().split())

if K > (N-1)*(N-2)//2:
    print(-1)
    exit()

print(N - 1 + (N - 1) * (N - 2) // 2 - K)
for i in range(2, N + 1):
    print(1, i, sep=" ")

c = 0
for i in range(2, N):
    for j in range(i + 1, N + 1):
        if (N - 1) * (N - 2) // 2 - K == c:
            exit()
        print(i, j, sep=" ")
        c += 1
