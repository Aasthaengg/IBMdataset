def resolve():
    # 整数 1 つ
    n = int(input())
    # 整数複数個
    # a, b, c = list(map(int, input().split()))
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    Asort = sorted(A)

    sumMed = 0
    for i in range(n):
        sumMed += Asort[n + i * 2]

    print(sumMed)

resolve()