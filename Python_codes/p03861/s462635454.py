def resolve():
    # 整数 1 つ
    # n = int(input())
    # 整数複数個
    a, b, x = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    if a % x == 0:
        nmin = int(a / x)
    else:
        nmin = (a // x) + 1

    nmax = b // x

    print(nmax - nmin +1)


resolve()