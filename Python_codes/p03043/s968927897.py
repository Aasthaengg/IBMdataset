N, K = list(map(int, input().split()))

ans = 0
for i in range(1, N+1):
    tmp = 0
    check = i
    for j in range(1, 100):
        if check >= K:
            ans += 1 / (N * 2 ** tmp)
            break
        tmp += 1
        check *= 2

print(ans)