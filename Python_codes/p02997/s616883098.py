
N, K = map(int, input().split())
res = (N - 1) * (N - 2) // 2 - K

if res < 0:
    print(-1)
else:
    ans = []
    for i in range(2, N + 1):
        ans.append([1, i])

    cnt = 0
    for i in range(2, N):
        if cnt == res:
            break

        for j in range(i + 1, N + 1):
            if cnt == res:
                break
            ans.append([i, j])
            cnt += 1

    print(len(ans))
    for v in ans:
        print(*v)
