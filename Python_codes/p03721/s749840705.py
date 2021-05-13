def resolve():
    N, K = [int(i) for i in input().split()]
    aabb = sorted([list(map(int, input().split())) for _ in range(N)])
    sumB = 0
    for a, b in aabb:
        sumB += b
        if sumB >= K:
            print(a)
            return


resolve()
