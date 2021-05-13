N, M, K = map(int, input().split())

ans = False
for n in range(0, N + 1):
    for m in range(0, M + 1):
        res = m * N + n * M - 2 * n * m
        if res == K:
            ans = True
            break

if ans:
    print("Yes")
else:
    print("No")
