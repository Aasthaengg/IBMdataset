def resolve():
    A, B, C, D = list(map(int, input().split()))
    area1 = A * B
    area2 = C * D
    print(max([area1, area2]))

resolve()