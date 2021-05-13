def resolve():
    # 整数 1 つ
    n = int(input())
    a = int(input())
    # 整数複数個
    # a, b, c = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    if n % 500 == 0:
        print("Yes")
    else:
        if n % 500 <= a:
            print("Yes")
        else:
            print("No")


resolve()