def resolve():
    N, M = list(map(int, input().split()))
    swi = []
    for i in range(M):
        k, *ss = list(map(int, input().split()))
        t = 0
        for s in ss:
            t += 1 << (s-1)
        swi.append(t)

    ps = list(map(int, input().split()))
    ans = 0
    for i in range(1 << N):
        for s, p in zip(swi, ps):
            t = i & s
            c = bin(t).count('1') % 2
            if c != p:
                break
        else:
            ans += 1
    print(ans)
    return

resolve()