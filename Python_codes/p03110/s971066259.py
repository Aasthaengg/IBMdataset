def resolve():
    BTC = 380000.0
    N = int(input())
    sumA = 0
    for _ in range(N):
        x, u = input().split()
        if u == "JPY":
            sumA += int(x)
        else:
            sumA += float(x) * BTC
    print(sumA)


resolve()
