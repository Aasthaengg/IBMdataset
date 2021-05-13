n, m = map(int, input().split())
denq = []
for _ in range(m):
    ks = tuple(map(lambda x: int(x)-1, input().split()))
    denq.append(set(ks[1:]))
P = tuple(map(int, input().split()))

ans = 0
for i in range(2**n):
    kk = [0] * m
    for j in range(n):
        # スイッチjがonの場合
        if (i>>j)&1:
            for idq, dq in enumerate(denq):
                # すべての電球に対して
                # スイッチjが電球に紐付けられていれば、onをカウント
                if j in dq:
                    kk[idq] += 1

    for idq in range(m):
        if P[idq] != kk[idq]%2:
            break
    else:
        ans += 1
print(ans)
