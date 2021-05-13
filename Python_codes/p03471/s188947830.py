N, Y = map(int, input().split())

loop_break = False
for M in range(2002):
    total = 10000 * M
    if total > Y:
        print(-1, -1, -1)
        break
    for G in range(N - M + 1):
        S = N - M - G
        total += 5000 * G + 1000 * S
        if total == Y:
            print(M, G, S)
            loop_break = True
            break
        else:
            total = 10000 * M
    if loop_break:
        break