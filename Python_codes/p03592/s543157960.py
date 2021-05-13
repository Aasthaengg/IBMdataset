N, M, K = map(int, input().split())
for a in range(N + 1):
    for b in range(M + 1):
        black = (a * M) + (b * N) - (a * b) * 2
        # print(a, b, black)
        if black == K:
            print("Yes")
            exit()
print("No")
