N = int(input())
ans = []
lis = []
for i in range(N):
    lis.append(i + 1)
if N % 2 == 0:
    M = (N - 2) * N // 2
    for i in range(1, N):
        for j in range(1, N):
            if j != i and i != lis[-j]:
                tmp = sorted([i, lis[-j]])
                if tmp not in ans:
                    ans.append(tmp)
    print(M)
    for i in range(M):
        print(' '.join(map(str, ans[i])))
else:
    M = (N - 1) ** 2 // 2
    for i in range(1, N):
        for j in range(2, N):
            if j != i + 1 and i != lis[-j]:
                tmp = sorted([i, lis[-j]])
                if tmp not in ans:
                    ans.append(tmp)
    for i in range(1, N):
        ans.append([N, i])
    print(M)
    for i in range(M):
        print(' '.join(map(str, ans[i])))