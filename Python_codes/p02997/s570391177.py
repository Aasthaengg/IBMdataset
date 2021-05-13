N, K = map(int, input().split())

if K > (N - 1) * (N - 2) // 2:
    print(-1)
else:
    M = N * (N - 1) // 2 - K
    cnt = 0
    ans = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            ans.append((i + 1, j + 1))
            cnt += 1
            if M == cnt:
                break
        else:
            continue
        break
    print(M)
    for edge in ans:
        print(*edge)
