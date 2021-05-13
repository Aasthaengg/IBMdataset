def resolve():
    N, K = list(map(int, input().split()))
    paint_way_count = K*(K-1)**(N-1)
    print(paint_way_count)

resolve()