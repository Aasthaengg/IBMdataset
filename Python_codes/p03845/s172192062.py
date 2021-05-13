def abc050_b():
    _ = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    Query = [tuple(map(int, input().split())) for _ in range(M)]

    tot = sum(T)
    for p, x in Query:
        ans = tot - T[p-1] + x
        print(ans)

abc050_b()