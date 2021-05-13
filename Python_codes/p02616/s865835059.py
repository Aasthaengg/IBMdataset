
N, K = map(int, input().split())
X = list(map(int, input().split()))

MOD = 10 ** 9 + 7

if K % 2 == 1 and all(v < 0 for v in X):
    # Minimize abs
    X.sort(key=lambda x: -x)
    ans = 1
    for i in range(K):
        ans = ans * X[i] % MOD
    print(ans)
elif K == N:
    ans = 1
    for i in range(K):
        ans = ans * X[i] % MOD
    print(ans)
else:
    pos = sorted(v for v in X if v >= 0)
    neg = sorted(-v for v in X if v < 0)

    ans = 1
    if K % 2 == 1:
        ans *= pos.pop()

    cand = []
    while len(pos) >= 2:
        tmp = pos.pop() * pos.pop()
        cand.append(tmp)

    while len(neg) >= 2:
        tmp = neg.pop() * neg.pop()
        cand.append(tmp)

    cand.sort(reverse=True)
    for i in range(K // 2):
        ans = ans * cand[i] % MOD

    print(ans)
