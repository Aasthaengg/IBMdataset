def resolve():
    N, M = list(map(int, input().split()))
    ls = []
    for _ in range(N):
        a, b = list(map(int, input().split()))
        ls.append([a, b])
    ls = sorted(ls, key=lambda x: x[0])
    ans = 0
    drink = 0
    for i in range(N):
        if drink >= M:
            break
        if drink + ls[i][1] >= M:
            ans += ls[i][0] * (M - drink)
            drink = M
        else:
            ans += ls[i][0] * ls[i][1]
            drink += ls[i][1]

    print(ans)
    return

resolve()