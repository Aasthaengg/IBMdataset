def resolve():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = 0
    for value, cost in zip(V, C):
        if value - cost > 0:
            ans += value - cost
    print(ans)


resolve()