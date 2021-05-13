def resolve():
    D, N = [int(i) for i in input().split()]
    print(100**D * (N + (N // 100)))


resolve()
