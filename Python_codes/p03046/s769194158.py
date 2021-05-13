M, K = map(int, input().split())

if 2 ** M <= K:
    print(-1)
    exit()

if K == 0:
    ans = []
    for i in range(2 ** M):
        ans.append(i)
        ans.append(i)
    print(*ans, sep=' ')
    exit()

X = [a for a in range(2 ** M) if (a != 0) and (a != K)]
N = len(X)
L = X[: N // 2][::-1] + [0] + [K] + X[: N // 2]
R = X[N // 2:] + [K] + [0] + X[N // 2:][::-1]
ans = L + R


zl, zr = [i for i, a in enumerate(ans) if a == 0]
check = 0
for a in ans[zl : zr]:
    check ^= a

if check == K:
    print(*ans, sep=' ')
else:
    print(-1)
