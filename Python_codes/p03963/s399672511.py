def resolve():
    # 整数 1 つ
    # n = int(input())
    # 整数複数個
    n, k = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    print(k*(k-1)**(n-1))


resolve()