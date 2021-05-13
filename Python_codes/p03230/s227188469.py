N = int(input())

for i in range(N + 1):
    if i * (i + 1) // 2 == N:
        M = i
        print('Yes')
        print(M + 1)
        res = [[] for _ in range(M + 1)]
        for i in range(M + 1):
            res[i].append(M)
        cnt = 1
        for k in range(M):
            for i in range(M - k):
                res[k].append(cnt + i)
            for i in range(M - k):
                res[k + i + 1].append(cnt)
                cnt += 1
        for r in res:
            print(*r)
        break
else:
    print('No')